# Generated by Django 3.2 on 2022-11-15 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0005_auto_20221006_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='showroomsupplieroffers',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='supplier_offers', to='supplier.supplier', verbose_name='Поставщик'),
        ),
    ]