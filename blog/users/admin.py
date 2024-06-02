from django.contrib import admin
from django.utils.html import format_html
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "image_display"]

    def image_display(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 45px; height:45px;" />', obj.image.url
            )
        return "No Image"

    image_display.short_description = "Image"
