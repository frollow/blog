from django.views.generic import CreateView

from .forms import ContactForm
from .models import Contact


class ContactViews(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "contacts/contact.html"
    success_url = "thank-you/"
