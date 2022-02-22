# Generated by Django 3.2.8 on 2021-12-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0019_alter_cart_cleaning_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cleaning_time',
            field=models.CharField(blank=True, choices=[('morning', '09.00 - 12.00'), ('afternoon', '12.00 - 15.00'), ('evening', '15.00 - 19.00')], max_length=15, verbose_name='Время уборки'),
        ),
    ]