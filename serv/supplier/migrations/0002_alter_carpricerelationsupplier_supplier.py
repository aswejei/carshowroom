# Generated by Django 3.2 on 2022-08-16 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpricerelationsupplier',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='supplier.supplier', verbose_name='Поставщик'),
        ),
    ]