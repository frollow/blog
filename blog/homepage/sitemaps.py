from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class MainSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return ["homepage:index"]

    def location(self, item):
        return reverse(item)
