# Generated by Django 3.1.2 on 2020-12-22 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]