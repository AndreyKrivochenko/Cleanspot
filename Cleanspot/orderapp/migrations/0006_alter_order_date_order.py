# Generated by Django 3.2.8 on 2021-12-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0005_auto_20211202_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_order',
            field=models.DateField(blank=True, null=True, verbose_name='Дата выполнения заказа'),
        ),
    ]
