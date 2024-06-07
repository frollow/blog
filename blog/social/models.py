from django.db import models


class Social(models.Model):
    SITE_TYPE_VALUES = (
        ("facebook", "Facebook"),
        ("instagram", "Instagram"),
        ("x", "X"),
        ("youtube", "YouTube"),
        ("linkedin", "LinkedIn"),
    )
    SITE_ICONS = {
        "facebook": "",
        "instagram": "",
        "x": "",
        "youtube": "",
        "linkedin": "",
    }
    SITE_URLS = {
        "facebook": "https://www.facebook.com/",
        "instagram": "https://www.instagram.com/",
        "x": "http://twitter.com/",
        "youtube": "https://www.youtube.com/",
        "linkedin": "https://www.linkedin.com/",
    }
    SITE_SHARE_LINKS = {
        "facebook": "sharer/sharer.php?u=",
        "instagram": "",
        "x": "share?url=",
        "youtube": "",
        "linkedin": "shareArticle?mini=true&url=",
    }
    site = models.CharField(
        max_length=20,
        choices=SITE_TYPE_VALUES,
        default="facebook",
        verbose_name="Site",
    )
    nickname = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Nickname",
    )
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

    def get_icon(self):
        """Returns the icon symbol for the site."""
        return self.SITE_ICONS.get(self.site, "")

    def get_base_url(self):
        """Returns the base URL for the site."""
        return self.SITE_URLS.get(self.site, "")

    def get_share_link(self):
        """Returns the share link template for the site."""
        return self.SITE_SHARE_LINKS.get(self.site, "")

    def __str__(self):
        return self.site

    class Meta:
        ordering = ("-last_modified_date",)
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
