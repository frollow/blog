# Generated by Django 5.0.4 on 2024-06-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0021_alter_post_group_alter_post_image_alter_post_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="text",
            field=models.TextField(verbose_name="Body"),
        ),
    ]
