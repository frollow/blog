# Generated by Django 5.0.4 on 2024-05-30 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0003_alter_social_site"),
    ]

    operations = [
        migrations.AddField(
            model_name="social",
            name="share_link",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Share link"
            ),
        ),
    ]
