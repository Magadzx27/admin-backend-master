# Generated by Django 3.1.4 on 2022-02-23 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20220224_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='preorder',
        ),
    ]
