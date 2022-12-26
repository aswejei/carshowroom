from typing import Dict, List

from django.db.models import Q

from serv.customer.models import Customer
from serv.supplier.models import CarPriceRelationSupplier, ShowroomSupplierOffers
from serv.carshowroom.models import CarPriceRelationShowroom, CarShowroom, CustomerShowroomOffers


def parse_dict_to_Q_expr(json_str: Dict) -> Q:
    """Parses showroom's JSONField with car characteristics and creates Q object of it's key - value entrances"""
    car_characteristics_dict = json_str.copy()
    final_q = Q()
    for key in car_characteristics_dict:
        if type(car_characteristics_dict[key]) == List:
            local_q = Q()
            for val in car_characteristics_dict[key]:
                local_q = local_q | Q(**{f'car__{key}': val})
            final_q = final_q & local_q
        elif type(car_characteristics_dict[key]) != Dict:
            final_q = final_q & Q(**{f'car__{key}': car_characteristics_dict[key]})
        else:
            pass
    return final_q


def buy_car_from_supplier(car_price_supplier: CarPriceRelationSupplier, showroom: CarShowroom, budget=None):
    """Buys car from supplier and adds it to showroom's car-price list"""
    try:
        car_price_showroom = CarPriceRelationShowroom.objects.filter(showroom__id=showroom.id)\
                                                             .select_related('car')\
                                                             .get(car__id=car_price_supplier.car.id)
    except CarPriceRelationShowroom.DoesNotExist:
        car_price_showroom = None
    if car_price_supplier.price_with_discount:
        budget -= car_price_supplier.price_with_discount
    else:
        budget -= car_price_supplier.price
    if car_price_showroom:
        car_price_showroom.quantity += 1
        car_price_showroom.save()
    else:
        car_price_showroom = CarPriceRelationShowroom.objects.create(
            car=car_price_supplier.car,
            showroom=showroom,
            price=car_price_supplier.price * 1.5,
            quantity=1
        )
        car_price_showroom.save()
    ShowroomSupplierOffers.objects.create(
        car=car_price_supplier.car,
        supplier=car_price_supplier.supplier,
        showroom=showroom,
        price=car_price_supplier.price_with_discount
    )
    return budget


def buy_car_from_showroom(car_price_showroom: CarPriceRelationShowroom, customer: Customer):
    if car_price_showroom:
        CustomerShowroomOffers.objects.create(
            customer=customer,
            showroom=car_price_showroom.showroom,
            car=car_price_showroom.car,
            price=car_price_showroom.price_with_discount
        )
        car_price_showroom.quantity -= 1
        if car_price_showroom.quantity == 1:
            car_price_showroom.safe_delete()
