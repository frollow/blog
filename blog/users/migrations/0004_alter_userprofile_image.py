# Generated by Django 5.0.4 on 2024-06-13 14:41

import core.utils
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_user_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="image",
            field=models.ImageField(
                blank=True, upload_to=core.utils.RenameImgPathToUsername("users/photo")
            ),
        ),
    ]
