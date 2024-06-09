from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.urls import reverse
from sorl.thumbnail import get_thumbnail

from .validators import (
    validate_file_extension,
    validate_image_size,
    validate_links_in_input,
    validate_post_name,
    validate_slug,
)

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        validators=[validate_post_name],
        max_length=100,
        verbose_name="Title",
        null=True,
        db_index=True,
    )
    slug = models.SlugField(
        validators=[validate_slug],
        max_length=50,
        unique=True,
        null=True,
        verbose_name="Slug",
    )
    short_text = models.TextField(
        max_length=95, verbose_name="Short text", blank=True, db_index=True
    )
    text = models.TextField(verbose_name="Body", validators=[validate_links_in_input])
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Author",
    )
    group = models.ForeignKey(
        "Group",
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Group",
        null=True,
    )
    image = models.ImageField(
        "Image",
        upload_to="posts/",
        validators=[validate_image_size, validate_file_extension],
    )
    feature = models.BooleanField(verbose_name="Feature", default=False)
    pub_date = models.DateTimeField(
        "Publish date", blank=True, null=True, db_index=True
    )
    paid = models.BooleanField(verbose_name="Paid", default=False)
    published = models.BooleanField(verbose_name="Published", default=False)
    added_date = models.DateTimeField(
        "Creation date",
        auto_now_add=True,
        null=True,
        blank=True,
        db_index=True,
    )
    last_modified_date = models.DateTimeField(
        "Updated date",
        auto_now=True,
        db_index=True,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.text[:15]

    def get_absolute_url(self):
        return reverse("posts:post_detail", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        # Set pub_date if not added in post
        if not self.pub_date:
            self.pub_date = timezone.now()
        super(Post, self).save(*args, **kwargs)

    @property
    def sd(self):
        if self.image:
            image_url = get_thumbnail(
                self.image,
                "500",
                crop="center",
                format="WEBP",
                upscale=False,
            ).url
        else:
            image_url = ""
        return {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "publisher": {
                "@type": "Organization",
                "name": "Wobidobi",
                "logo": "https://wobidobi.com/static/images/logo.svg",
            },
            "headline": self.title,
            "url": self.slug,
            "mainEntityOfPage": self.slug,
            "articleBody": self.text,
            "image": image_url,
            "datePublished": self.pub_date.isoformat() if self.pub_date else "",
            "dateModified": self.last_modified_date.isoformat()
            if self.last_modified_date
            else "",
            "author": {
                "@type": "Person",
                "name": self.author.get_full_name() or self.author.username,
            },
        }

    class Meta:
        ordering = ("-pub_date",)
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Group name")
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name="Slug",
    )
    description = models.TextField(verbose_name="Group description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Comment(models.Model):
    text = models.TextField(verbose_name="Comment")
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Article",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="Author",
    )
    created = models.DateTimeField(
        "Created date",
        auto_now_add=True,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
        verbose_name="Follower",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
        verbose_name="Following",
    )

    class Meta:
        verbose_name = "Follow"
        verbose_name_plural = "Follows"
        constraints = [
            models.UniqueConstraint(fields=["user", "author"], name="unique_followers"),
        ]
