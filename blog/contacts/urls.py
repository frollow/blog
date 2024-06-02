from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.ContactViews.as_view(), name="contact"),
    path("thank-you/", TemplateView.as_view(template_name="contacts/thank_you.html")),
]
