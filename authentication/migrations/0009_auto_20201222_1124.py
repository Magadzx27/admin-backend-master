# Generated by Django 3.1.2 on 2020-12-22 03:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20201218_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
