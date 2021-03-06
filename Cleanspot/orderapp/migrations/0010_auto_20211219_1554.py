# Generated by Django 3.2.8 on 2021-12-19 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orderapp', '0009_auto_20211210_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Ключ сессии'),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, verbose_name='Заказчик'),
        ),
    ]
