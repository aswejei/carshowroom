# Generated by Django 3.2 on 2022-10-04 08:43

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarPriceRelationShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('price_with_discount', models.FloatField(default=None, null=True, verbose_name='Цена со скидкой')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(verbose_name='Количество автомобилей в наличии')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['showroom', 'car'],
            },
        ),
        migrations.CreateModel(
            name='CarShowroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название автосалона')),
                ('location', django_countries.fields.CountryField(max_length=2, verbose_name='Местоположение автосалона')),
                ('car_characteristics', models.JSONField(verbose_name='Список характеристик покупаемых автомобилей')),
                ('description', models.TextField(max_length=500, verbose_name='Описание')),
                ('balance', models.FloatField(default=1000000, verbose_name='Баланс автосалона')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerShowroomOffers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('is_active', models.BooleanField(default=True)),
                ('offer_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
