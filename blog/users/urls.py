from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.urls import path

from . import views
from .forms import (
    AccountLoginForm,
    AccountPasswordChangeForm,
    AccountPasswordResetConfirmForm,
    AccountPasswordResetForm,
)

app_name = "users"

urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("signup-done/", views.SignUpDone.as_view(), name="signup_done"),
    path(
        "logout/",
        LogoutView.as_view(template_name="users/logged_out.html"),
        name="logout",
    ),
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html",
            authentication_form=AccountLoginForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path(
        "password_reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            form_class=AccountPasswordResetForm,
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html",
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            form_class=AccountPasswordResetConfirmForm,
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html",
        ),
        name="password_reset_complete",
    ),
    path(
        "password_change/",
        PasswordChangeView.as_view(
            template_name="users/password_change_form.html",
            form_class=AccountPasswordChangeForm,
        ),
        name="password_change",
    ),
    path(
        "password_change/done/",
        PasswordChangeDoneView.as_view(
            template_name="users/password_change_done.html",
        ),
        name="password_change_done",
    ),
]
