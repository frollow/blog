# Generated by Django 5.0.4 on 2024-06-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_userprofile_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="ai_bot",
            field=models.BooleanField(blank=True, null=True, verbose_name="AI Bot"),
        ),
    ]
