from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Full name")
    email = models.EmailField(verbose_name="Email Address", blank=False)
    phone_number = models.CharField(verbose_name="Phone", max_length=15)
    subject = models.CharField(max_length=50, verbose_name="Subject")
    message = models.TextField(verbose_name="Leave us a message", max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
