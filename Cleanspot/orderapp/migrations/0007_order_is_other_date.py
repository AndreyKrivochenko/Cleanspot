# Generated by Django 3.2.8 on 2021-12-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0006_alter_order_date_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_other_date',
            field=models.BooleanField(default=False, verbose_name='Готов рассмотреть другие даты уборки'),
        ),
    ]
