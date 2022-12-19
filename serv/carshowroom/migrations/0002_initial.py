# Generated by Django 3.2 on 2022-10-04 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carshowroom', '0001_initial'),
        ('supplier', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customershowroomoffers',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='supplier.car', verbose_name='Автомобиль'),
        ),
        migrations.AddField(
            model_name='customershowroomoffers',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='offers', to='customer.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='customershowroomoffers',
            name='showroom',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='carshowroom.carshowroom', verbose_name='Автосалон'),
        ),
    ]
