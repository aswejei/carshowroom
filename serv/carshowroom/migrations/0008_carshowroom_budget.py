# Generated by Django 3.2 on 2022-11-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carshowroom', '0007_alter_customershowroomoffers_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='carshowroom',
            name='budget',
            field=models.FloatField(default=0.1, verbose_name='Процент от баланса который тратится на закупки'),
        ),
    ]
