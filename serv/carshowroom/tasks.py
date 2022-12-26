from celery import shared_task
from django.db.models import Q

from serv.supplier.models import CarPriceRelationSupplier
from serv.core.operations import parse_dict_to_Q_expr, buy_car_from_supplier
from serv.carshowroom.models import CarShowroom, CarPriceRelationShowroom, CustomerShowroomOffers


@shared_task()
def buy_cars():
    for showroom in CarShowroom.objects.filter(is_active=True):
        q_expr = parse_dict_to_Q_expr(showroom.car_characteristics)
        car_price_query = CarPriceRelationSupplier.objects.filter(is_active=True) \
                                                          .filter(q_expr) \
                                                          .order_by('price_with_discount')
        budget = showroom.balance * showroom.budget
        for car in car_price_query:
            if car.price_with_discount is not None:
                if car.price_with_discount <= budget:
                    budget = buy_car_from_supplier(car, showroom, budget=budget)
                else:
                    break
            else:
                if car.price <= budget:
                    budget = buy_car_from_supplier(car, showroom, budget=budget)


@shared_task()
def generate_offer(max_price=None, characteristics_dict=None, request=None):
    q_expr = parse_dict_to_Q_expr(characteristics_dict)
    car_price = CarPriceRelationShowroom.objects.filter(is_active=True) \
                                                .filter(Q(**{'price_with_discount__lte': max_price})) \
                                                .filter(q_expr)\
                                                .order_by('price_with_discount')\
                                                .first()
    if car_price:
        offer = CustomerShowroomOffers.objects.create(
            car=car_price.car,
            customer=request.user.customer_profile,
            showroom=car_price.showroom,
            price=car_price.price_with_discount
        )
        return offer
