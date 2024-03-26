# Generated by Django 3.1.2 on 2020-11-11 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_method', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shipping_method',
            name='contact_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shipping_method',
            name='image_url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]