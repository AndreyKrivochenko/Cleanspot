# Generated by Django 3.2.8 on 2021-12-03 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0002_servicetype_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserTypeForServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название типа пользователя')),
                ('description', models.CharField(max_length=128, verbose_name='Описание типа пользователя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('slug', models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Тип пользователя для типа услуг',
                'verbose_name_plural': 'Типы пользователей для типов услуг',
            },
        ),
        migrations.AddField(
            model_name='servicetype',
            name='user_type_for_service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cartapp.usertypeforservicetype', verbose_name='Тип пользователя для типа услуг'),
        ),
    ]