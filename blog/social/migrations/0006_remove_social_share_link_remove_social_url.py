# Generated by Django 5.0.4 on 2024-06-08 13:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0005_social_nickname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="social",
            name="share_link",
        ),
        migrations.RemoveField(
            model_name="social",
            name="url",
        ),
    ]
