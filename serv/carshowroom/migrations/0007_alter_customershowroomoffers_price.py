# Generated by Django 3.2 on 2022-10-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshowroom', '0006_auto_20221006_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customershowroomoffers',
            name='price',
            field=models.FloatField(verbose_name='Цена подобранного автомобиля'),
        ),
    ]
