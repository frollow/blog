from core.utils import RenameImgPathToUsername
from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_name, validate_username


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Log in",
        validators=[validate_username],
        help_text="Can only contain lowercase Latin letters, numbers, and hyphens.",
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name="Name",
        validators=[validate_name],
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name="Second name",
        validators=[validate_name],
    )
    email = models.EmailField(unique=True)
    email_confirmed = models.BooleanField(
        default=False,
        verbose_name="Email confirmed",
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    image = models.ImageField(
        upload_to=RenameImgPathToUsername("users/photo"), blank=True
    )

    def __str__(self):
        return self.user.username
