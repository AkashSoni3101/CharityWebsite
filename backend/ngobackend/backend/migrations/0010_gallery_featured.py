# Generated by Django 3.2.9 on 2021-11-23 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_gallery_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]