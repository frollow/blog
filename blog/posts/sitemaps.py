from django.contrib.auth import get_user_model
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Post, Group

User = get_user_model()


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = "https"

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date


class GroupSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "https"

    def items(self):
        return Group.objects.all()

    def lastmod(self, obj):
        return obj.last_modified_date


class ProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = "https"

    def items(self):
        return User.objects.all()

    def location(self, obj):
        return reverse("posts:profile", kwargs={"username": obj.username})

    def lastmod(self, obj):
        if obj.posts.exists():
            return obj.posts.latest("last_modified_date").last_modified_date
        return None
