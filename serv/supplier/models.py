from django.db import models

from user.models import User


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
    staff = models.ManyToManyField(User)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} (founded: {self.date_founded})'

    def safe_delete(self):
        self.is_active = False
        self.save()
        for obj in self.cars.all():
            obj.is_active = False
            obj.save()


class Car(models.Model):
    _car_body_choices = [
        ('SE', 'Sedan'),
        ('CO', 'Coupe'),
        ('SC', 'Sports car'),
        ('SW', 'Station wagon'),
        ('HB', 'Hatchback'),
        ('CT', 'Convertible'),
        ('SUV', 'Sport-Utility vehicle'),
        ('MV', 'Minivan'),
        ('PUT', 'Pick-up truck'),
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
        choices=_car_body_choices,
        verbose_name='Тип кузова',
        max_length=20
    )
    is_active = models.BooleanField(default=True)

    def safe_delete(self):
        self.is_active = False
        self.save()
        for i in self.supplier_car_prices.all():
            i.is_active = False
            i.save()

    def __str__(self):
        return f'{self.brand} {self.model} (color: {self.color})'

    class Meta:
        unique_together = ['brand', 'model', 'color', 'engine_v', 'car_body']


class CarPriceRelation(models.Model):
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name='Автомобиль',
        related_name="%(app_label)s_car_prices"
    )
    price = models.FloatField(verbose_name='Цена')
    price_with_discount = models.FloatField(verbose_name='Цена со скидкой', blank=True, default=None, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CarPriceRelationSupplier(CarPriceRelation):
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        verbose_name='Поставщик',
        related_name='cars'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.car.brand} {self.car.model} - {self.price}$ : {self.supplier.name}'

    def safe_delete(self):
        self.is_active = False
        self.save()

    class Meta:
        ordering = [
            'supplier',
            'car',
        ]
        unique_together = [
            'car',
            'supplier',
        ]


class ShowroomSupplierOffers(models.Model):
    showroom = models.ForeignKey(
        'carshowroom.CarShowroom',
        on_delete=models.PROTECT,
        verbose_name='Автосалон'
    )
    supplier = models.ForeignKey(
        Supplier,
        models.PROTECT,
        verbose_name='Поставщик',
        related_name="%(app_label)s_offers"
    )
    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        verbose_name='Автомобиль'
    )
    price = models.FloatField(verbose_name='Цена')
    date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = [
            '-date',
            'showroom',
        ]
