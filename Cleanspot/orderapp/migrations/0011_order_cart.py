# Generated by Django 3.2.8 on 2021-12-20 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0026_auto_20211210_0952'),
        ('orderapp', '0010_auto_20211219_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cartapp.cart', verbose_name='Корзина'),
        ),
    ]
