import logging

from celery import shared_task
from celery_singleton import Singleton
from django.core.files.base import ContentFile
from django.db import IntegrityError
from django.utils import timezone
from links.models import ProcessedLink

from .models import Group, Post, User
from .openai_client import generate_image_from_openai, request_to_openai
from .utils import (
    clean_html,
    fetch_article_text,
    fetch_rss_items,
    generate_unique_slug,
    strip_html_tags,
)

logger = logging.getLogger('posts')


@shared_task(base=Singleton, singleton_key="fetch_and_create_post", singleton_lock_expiry=60*10)
def fetch_and_create_post():
    logger.debug("fetch_and_create_post task started")
    rss_url = "https://www.yahoo.com/tech/rss"
    items = fetch_rss_items(rss_url, limit=50)

    if not items:
        logger.debug("No articles found in the RSS feed.")
        return

    for item in items:
        title, link = item["title"], item["link"]

        if ProcessedLink.objects.filter(link=link).exists():
            logger.info(f"Link already processed: {link}")
            continue

        article_text = fetch_article_text(link)
        if not article_text:
            continue

        summary_content = request_to_openai(
            prompt=(
                f"Please summarize and paraphrase the following text into 3000 characters. "
                f"Do not include any information about authors or sources. "
                f"Ensure the entire text is written from the perspective of a journalist. "
                f"Use only the following HTML tags: <p>, <h2>, <h3>, <h4>, <h5>.\n\n{article_text}"
            ),
            model="gpt-4o-2024-05-13"
        )
        if not summary_content:
            continue

        summary_content = clean_html(summary_content)

        short_text = strip_html_tags(summary_content)[:95]

        rephrased_title = request_to_openai(
            prompt=f"Please paraphrase the following title into 66 characters:\n\n{title}",
            model="gpt-4o-2024-05-13"
        )
        if not rephrased_title:
            continue

        slug = generate_unique_slug(Post, rephrased_title)
        if len(slug) > 50:
            slug = slug[:50]
        image_content = generate_image_from_openai(rephrased_title)
        if not image_content:
            continue

        image_file = ContentFile(image_content, name=f"{slug}.png")
        author = User.objects.first()
        group = Group.objects.get(id=1)

        if not ProcessedLink.objects.filter(link=link).exists():
            try:
                ProcessedLink.objects.create(link=link)
            except IntegrityError:
                logger.error("Failed to add link to ProcessedLink.")
            try:
                logger.info("Start post creation")
                Post.objects.create(
                    title=rephrased_title.strip(),
                    slug=slug,
                    short_text=short_text,
                    text=summary_content,
                    author=author,
                    pub_date=timezone.now(),
                    published=True,
                    image=image_file,
                    group=group,
                )
                logger.info(f"Post created: {rephrased_title.strip()}")
            except IntegrityError:
                logger.error(f"Failed to create post: Duplicate slug for {rephrased_title.strip()}")
        else:
            logger.info(f"Link: {link} alredy in database. Post not created")
