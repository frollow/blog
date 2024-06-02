from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from .models import Contact


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(label="", widget=ReCaptchaV3())

    class Meta:
        model = Contact
        fields = (
            "name",
            "email",
            "phone_number",
            "subject",
            "message",
        )

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "256",
                    "autofocus": True,
                    "placeholder": "ex. John Carter",
                }
            ),
            "email": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "256",
                    "placeholder": "example@email.com",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "15",
                    "placeholder": "(123) 456 - 789",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "maxlength": "256",
                    "placeholder": "ex. Subscriptions",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "text-area w-input",
                    "rows": 3,
                    "style": "resize:vertical",
                    "maxlength": "5000",
                    "spellcheck": "false",
                    "placeholder": "Please type your message here...",
                }
            ),
        }
