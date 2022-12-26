from celery import shared_task

from django.db.models import F
from django.db.models.lookups import LessThan

from serv.customer.models import Customer
from serv.core.operations import buy_car_from_showroom
from serv.carshowroom.models import CarPriceRelationShowroom


@shared_task()
def buy_cars():
    for customer in Customer.objects.filter(is_active=True):
        car = CarPriceRelationShowroom.objects.filter(LessThan(F('price_with_discount'), customer.balance/5))\
                                              .order_by('-date_added')\
                                              .first()
        buy_car_from_showroom(car, customer)
