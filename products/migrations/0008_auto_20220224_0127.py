# Generated by Django 3.1.4 on 2022-02-23 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201227_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='price',
        ),
        migrations.RemoveField(
            model_name='products',
            name='stock',
        ),
    ]
