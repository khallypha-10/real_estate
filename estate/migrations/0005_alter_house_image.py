# Generated by Django 4.1.6 on 2023-02-05 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0004_alter_house_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
