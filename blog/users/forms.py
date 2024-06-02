from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    PasswordResetForm,
    SetPasswordForm,
    UserCreationForm,
    UsernameField,
)

from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

from .models import UserProfile

User = get_user_model()


class CreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CreationForm, self).__init__(*args, **kwargs)
        # Remove label='' for each field
        for field_name, field in self.fields.items():
            field.label = ""

    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "placeholder": "Password"},
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "placeholder": "Confirm password"},
        ),
    )
    captcha = ReCaptchaField(label="", widget=ReCaptchaV3())

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("first_name", "last_name", "username", "email")
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "autofocus": True,
                    "placeholder": "First name",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "placeholder": "Last name",
                },
            ),
            "username": forms.TextInput(
                attrs={
                    "class": "input w-input",
                    "placeholder": "Username",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "input w-input",
                    "placeholder": "Email",
                },
            ),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]


class AccountLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={"class": "input w-input", "autofocus": True, "placeholder": "Username"}),
        label="",
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "autocomplete": "current-password", "placeholder": "Password"},
        ),
        label="",
    )


class AccountPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "input w-input", "autofocus": True, "placeholder": "Email"}),
        label="",
    )


class AccountPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "autofocus": True, "placeholder": "New password"},
        ),
        label="",
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "placeholder": "Confirm password"},
        ),
        label="",
    )


class AccountPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "placeholder": "Previous password"},
        ),
        label="",
    )
    new_password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "placeholder": "New password"},
        ),
        label="",
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={"class": "input w-input", "placeholder": "Confirm password"},
        ),
        label="",
    )
