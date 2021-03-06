# Generated by Django 3.2.9 on 2021-11-30 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_rename_volunteer_becomevolunteer'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Head', 'Head'), ('Volunteer', 'Volunteeer'), ('Public', 'Public')], default='Head', max_length=50)),
                ('thumbnail', models.ImageField(upload_to='team/%Y/%m/%d')),
                ('message', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
