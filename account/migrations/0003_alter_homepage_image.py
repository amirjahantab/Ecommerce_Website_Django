# Generated by Django 4.1.1 on 2023-11-24 17:00

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ImageField(upload_to=account.models.get_home_image_filepath),
        ),
    ]
