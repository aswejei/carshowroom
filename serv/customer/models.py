from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=20)
    surname = models.CharField(verbose_name='Фамилия', max_length=20)
    balance = models.FloatField(verbose_name='Баланс')
    is_active = models.BooleanField(default=True)
