import datetime

import django.utils.timezone

from supplier.models import CarPriceRelation

from django.db import models
from django_countries.fields import CountryField


# Create your models here.
from user.models import User


class CarShowroom(models.Model):
    name = models.CharField(
        verbose_name='Название автосалона',
        max_length=30
    )
    location = CountryField(verbose_name='Местоположение автосалона')
    car_characteristics = models.JSONField(verbose_name='Список характеристик покупаемых автомобилей')
    description = models.TextField(
        max_length=500,
        verbose_name='Описание'
    )
    balance = models.FloatField(verbose_name='Баланс автосалона', default=1000000)
    budget = models.FloatField(verbose_name='Процент от баланса который тратится на закупки', default=0.1)
    staff = models.ManyToManyField(User)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} ({self.location})'

    def safe_delete(self):
        self.is_active = False
        self.save()
        for obj in self.cars.all():
            obj.is_active = False
            obj.save()


class CustomerShowroomOffers(models.Model):
    customer = models.ForeignKey(
        'customer.Customer',
        on_delete=models.PROTECT,
        verbose_name='Покупатель',
        related_name='offers'
    )
    showroom = models.ForeignKey(
        CarShowroom,
        on_delete=models.PROTECT,
        verbose_name='Автосалон'
    )
    car = models.ForeignKey(
        'supplier.Car',
        on_delete=models.PROTECT,
        verbose_name='Автомобиль'
    )
    price = models.FloatField(verbose_name='Цена подобранного автомобиля')
    is_active = models.BooleanField(default=True)
    offer_date = models.DateTimeField(default=django.utils.timezone.now)


class CarPriceRelationShowroom(CarPriceRelation):
    quantity = models.IntegerField(verbose_name='Количество автомобилей в наличии')
    showroom = models.ForeignKey(
        CarShowroom,
        on_delete=models.CASCADE,
        verbose_name='Автосалон',
        related_name='cars'
    )
    is_active = models.BooleanField(default=True)

    def safe_delete(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return f'{self.car.brand} {self.car.model} - {self.price}$ : {self.showroom.name}'

    class Meta:
        ordering = ['showroom', 'car']
        unique_together = ['showroom', 'car']
