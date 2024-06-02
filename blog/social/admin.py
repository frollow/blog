from django.contrib import admin
from .models import Social


class SocialAdmin(admin.ModelAdmin):
    list_display = ("pk", "site", "last_modified_date")
    empty_value_display = "-empty-"


admin.site.register(Social, SocialAdmin)
