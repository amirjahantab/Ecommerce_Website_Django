# Generated by Django 4.1.1 on 2023-11-30 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_homepage_first_description_services_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='seccond_description_services',
            new_name='second_description_services',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='seccond_title_services',
            new_name='second_title_services',
        ),
    ]