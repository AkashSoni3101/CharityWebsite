# Generated by Django 3.2.9 on 2021-11-23 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20211123_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]