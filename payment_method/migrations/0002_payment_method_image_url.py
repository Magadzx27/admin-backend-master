# Generated by Django 3.1.2 on 2020-11-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_method', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_method',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]