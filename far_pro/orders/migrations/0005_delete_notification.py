# Generated by Django 5.0.7 on 2024-07-16 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
