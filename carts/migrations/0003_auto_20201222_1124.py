# Generated by Django 3.1.2 on 2020-12-22 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20201213_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='quantity',
            field=models.DecimalField(decimal_places=0, max_digits=5),
        ),
    ]