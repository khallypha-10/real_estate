# Generated by Django 4.1.6 on 2023-02-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_house_added_house_last_updated_alter_house_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(null=True, upload_to='estate/static/media'),
        ),
    ]