# Generated by Django 3.2.9 on 2022-01-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('donation_Amount', models.CharField(max_length=25)),
                ('donation_PaymentID', models.CharField(max_length=100)),
                ('isPaid', models.BooleanField(default=False)),
                ('donation_Date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]