# Generated by Django 3.2.7 on 2021-11-07 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cleanspotuser',
            name='name_display_site',
        ),
    ]
