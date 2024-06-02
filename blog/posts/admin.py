from django.contrib import admin

from .models import Follow, Comment, Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "pub_date", "author")
    search_fields = (
        "tirle",
        "text",
        "author",
    )
    list_filter = ("pub_date",)
    empty_value_display = "-empty-"


admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "slug", "description")
    search_fields = (
        "title",
        "slug",
    )
    empty_value_display = "-empty-"
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Group, GroupAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "created", "post", "author")
    search_fields = ("text",)
    empty_value_display = "-empty-"


admin.site.register(Comment, CommentAdmin)


class FollowAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "user")
    empty_value_display = "-empty-"


admin.site.register(Follow, FollowAdmin)
