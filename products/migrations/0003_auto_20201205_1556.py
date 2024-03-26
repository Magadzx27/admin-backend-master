# Generated by Django 3.1.2 on 2020-12-05 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0002_auto_20201205_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_id',
            field=models.OneToOneField(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='categories.category'),
        ),
    ]