# Generated by Django 3.2.8 on 2021-12-09 09:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0023_cart_is_windows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='windows',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cartapp.windowwashing', verbose_name='Окна'),
        ),
    ]
