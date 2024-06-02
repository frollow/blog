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
    site = models.CharField(
        max_length=20,
        choices=SITE_TYPE_VALUES,
        default="facebook",
        verbose_name="Site",
    )
    url = models.URLField(
        max_length=100,
        verbose_name="URL",
        blank=True,
        null=True,
    )
    share_link = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Share link",
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

    def __str__(self):
        return self.site

    class Meta:
        ordering = ("-last_modified_date",)
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
