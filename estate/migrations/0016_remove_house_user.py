# Generated by Django 4.1.6 on 2023-02-08 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0015_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='user',
        ),
    ]
