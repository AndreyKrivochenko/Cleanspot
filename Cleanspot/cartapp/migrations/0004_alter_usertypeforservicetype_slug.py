# Generated by Django 3.2.8 on 2021-12-03 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0003_auto_20211203_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertypeforservicetype',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
    ]