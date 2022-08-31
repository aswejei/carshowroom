from django.db import models


# Create your models here.
from users.models import CustomUser


class Customer(models.Model):
    related_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Покупатель')
    balance = models.FloatField(verbose_name='Баланс')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'
