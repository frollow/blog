import logging
import random
import re

import requests
from bs4 import BeautifulSoup
from django.template.loader import render_to_string
from django.utils.timezone import localtime

logger = logging.getLogger("posts")


def fetch_rss_items(rss_url, limit):
    response = requests.get(rss_url)
    if response.status_code != 200:
        logger.error(
            f"Failed to retrieve the RSS feed. Status code: {response.status_code}"
        )
        return []

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")[:limit]

    return [
        {"title": item.find("title").get_text(), "link": item.find("link").get_text()}
        for item in items
    ]


def fetch_article_text(link):
    article_response = requests.get(link)
    if article_response.status_code != 200:
        logger.error(
            f"Failed to retrieve the article. Status code: {article_response.status_code}"
        )
        return None

    article_soup = BeautifulSoup(article_response.content, "html.parser")
    caas_body = article_soup.find(class_="caas-body")

    if not caas_body:
        logger.error(f"No caas-body found in the article: {link}")
        return None

    # Extracting text, ignoring texts wrapped in links
    paragraphs = []
    for element in caas_body.find_all(["p", "h2", "h3", "h4", "h5"]):
        text_parts = []
        for content in element.contents:
            if content.name == "a":
                continue
            if isinstance(content, str):
                text_parts.append(content)
            elif hasattr(content, "get_text"):
                text_parts.append(content.get_text())
        paragraphs.append("".join(text_parts))

    article_text = " ".join(paragraphs)
    return article_text


def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    allowed_tags = {"p", "h2", "h3", "h4", "h5"}

    for tag in soup.find_all():
        if tag.name not in allowed_tags:
            tag.unwrap()  # Removing the tag but keeping the content

    return str(soup)


def generate_unique_slug(model_class, title, max_attempts=10):
    slug = re.sub(r"\W+", "-", title.lower()).strip("-")
    for attempt in range(max_attempts):
        if not model_class.objects.filter(slug=slug).exists():
            return slug
        slug = f"{slug}-{attempt + 1}"
    raise ValueError(f"Unable to generate a unique slug for title: {title}")


def insert_advertisement(text, template: str):
    # Render the advertisement template
    ad_html = render_to_string(template)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(text, "html.parser")

    # Find all paragraph tags
    paragraphs = soup.find_all("p")

    # Check if there are at least two paragraphs
    if len(paragraphs) > 2:
        # Create a new BeautifulSoup object for the advertisement
        ad_soup = BeautifulSoup(ad_html, "html.parser")

        # Insert the advertisement after the second paragraph
        paragraphs[1].insert_after(ad_soup)

    # Return the modified HTML as a string
    return str(soup)


def get_random_ai_author(model):
    ai_authors = model.objects.filter(ai_bot=True)
    if ai_authors.exists():
        return random.choice(ai_authors)
    else:
        return model.objects.first()


def format_datetime_to_iso(datetime_field):
    formatted_date = localtime(datetime_field).strftime('%Y-%m-%dT%H:%M:%S%z')
    # ISO 8601 convert "+0000" в "+00:00"
    formatted_date = formatted_date[:-2] + ':' + formatted_date[-2:]
    return formatted_date
