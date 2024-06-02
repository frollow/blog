from django.contrib import admin

from .models import ProcessedLink


class ProcessedLinkAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "link",
        "processed_at",
    )
    empty_value_display = "-empty-"


admin.site.register(ProcessedLink, ProcessedLinkAdmin)
