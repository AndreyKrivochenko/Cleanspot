# Generated by Django 3.2.8 on 2021-12-09 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0024_alter_cart_windows'),
    ]

    operations = [
        migrations.AddField(
            model_name='windowwashing',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cartwindows', to='cartapp.cart', verbose_name='Корзина'),
        ),
        migrations.RemoveField(
            model_name='cart',
            name='windows',
        ),
        migrations.AddField(
            model_name='cart',
            name='windows',
            field=models.ManyToManyField(blank=True, related_name='related_cart_window', to='cartapp.WindowWashing', verbose_name='Мойка окон'),
        ),
    ]
