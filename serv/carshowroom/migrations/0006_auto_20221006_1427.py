# Generated by Django 3.2 on 2022-10-06 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_user'),
        ('supplier', '0004_alter_carpricerelationsupplier_price_with_discount'),
        ('carshowroom', '0005_alter_carpricerelationshowroom_price_with_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customershowroomoffers',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='supplier.car', verbose_name='Автомобиль'),
        ),
        migrations.AlterField(
            model_name='customershowroomoffers',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='offers', to='customer.customer', verbose_name='Покупатель'),
        ),
        migrations.AlterField(
            model_name='customershowroomoffers',
            name='showroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='carshowroom.carshowroom', verbose_name='Автосалон'),
        ),
    ]