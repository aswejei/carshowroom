# Generated by Django 3.2 on 2022-10-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(verbose_name='Баланс')),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
