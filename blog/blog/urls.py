from contacts.sitemaps import ContactSitemap
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from homepage.sitemaps import MainSitemap
from posts.sitemaps import GroupSitemap, PostSitemap, ProfileSitemap
from posts.views import generate_news_sitemap

sitemaps = {
    "main": MainSitemap,
    "posts": PostSitemap,
    "group": GroupSitemap,
    "profiles": ProfileSitemap,
    "contacts": ContactSitemap,
}

urlpatterns = [
    path("auth/", include(("users.urls", "users"), namespace="users")),
    path("auth/", include("django.contrib.auth.urls")),
    path("admindd/", admin.site.urls),
    path("posts/", include(("posts.urls", "posts"), namespace="posts")),
    path("", include(("homepage.urls", "homepage"), namespace="homepage")),
    path("contacts/", include("contacts.urls", namespace="contacts")),
    path("search", include("search.urls", namespace="search")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("sitemap-news.xml", generate_news_sitemap, name="news_sitemap"),
    path("cookies/", include("cookie_consent.urls")),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "core.views.page_not_found"
handler500 = "core.views.server_error"
handler403 = "core.views.permission_denied"

admin.site.site_header = "Wobidobi - Admin Panel"
admin.site.site_title = "Wobidobi"
admin.site.index_title = "Welcome to the Admin Interface!"


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
