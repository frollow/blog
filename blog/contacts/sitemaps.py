from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class ContactSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return ["contacts:contact"]

    def location(self, item):
        return reverse(item)
