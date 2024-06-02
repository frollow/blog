from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "date")
    search_fields = (
        "name",
        "email",
        "message",
    )
    list_filter = ("date",)
    empty_value_display = "-empty-"


admin.site.register(Contact, ContactAdmin)
