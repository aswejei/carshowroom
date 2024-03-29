from django.db import models

from serv.user.models import User


class Customer(models.Model):
    balance = models.FloatField(verbose_name='Баланс')
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')

