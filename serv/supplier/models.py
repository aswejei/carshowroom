from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class Supplier(models.Model):
    name = models.CharField(
        verbose_name='Название поставщика',
        max_length=30
    )
    date_founded = models.DateField(verbose_name='Дата основания')
    description = models.TextField(
        verbose_name='Описание',
        max_length=500
    )
    is_active = models.BooleanField(default=True)


class Car(models.Model):
    car_body_choices = [
        ('SE', 'Sedan'),
        ('CO', 'Coupe'),
        ('SC', 'Sports car'),
        ('SW', 'Station wagon'),
        ('HB', 'Hatchback'),
        ('CT', 'Convertible'),
        ('SUV', 'Sport-Utility vehicle'),
        ('MV', 'Minivan'),
        ('PUT', 'Pick-up truck')
    ]
    brand = models.CharField(
        verbose_name='Производитель',
        max_length=20
    )
    model = models.CharField(
        verbose_name='Модель',
        max_length=20
    )
    color = models.CharField(
        verbose_name='Цвет',
        max_length=20
    )
    engine_v = models.FloatField(verbose_name='Объем двигателя')
    car_body = models.CharField(
        choices=car_body_choices,
        verbose_name='Тип кузова',
        max_length=20
    )
    is_active = models.BooleanField(default=True)


class CarPriceRelation(models.Model):
    car = models.OneToOneField(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль'
    )
    price = models.IntegerField(verbose_name='Цена')
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CarPriceRelationSupplier(CarPriceRelation):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='Поставщик'
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['supplier', 'car']


class ShowroomSupplierOffers(models.Model):
    showroom = models.OneToOneField(
        'carshowroom.CarShowroom',
        on_delete=models.PROTECT,
        verbose_name='Автосалон'
    )
    supplier = models.OneToOneField(
        Supplier,
        models.PROTECT,
        verbose_name='Поставщик'
    )
    car = models.OneToOneField(
        Car,
        on_delete=models.PROTECT,
        verbose_name='Автомобиль'
    )
    price = models.FloatField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date', 'showroom']
