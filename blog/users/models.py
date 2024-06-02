from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    image = models.ImageField(upload_to="user_images/", blank=True)

    def __str__(self):
        return self.user.username
