import datetime

from django.contrib import admin

from models import CarShowroom, CustomerShowroomOffers, CarPriceRelationShowroom
from serv.customer.models import Customer


@admin.register(CarShowroom)
class CarShowroomAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'amount_of_sold_cars', 'top_customer', 'last_month_income']

    def amount_of_sold_cars(self, obj):
        result = CustomerShowroomOffers.objects.filter(showroom=obj).count()
        return result

    def top_customer(self, obj):
        from django.db.models import Count
        if CustomerShowroomOffers.objects.filter(showroom=obj).first():
            customer = Customer.objects.get(id=CustomerShowroomOffers.objects.filter(showroom=obj).values('customer') \
                                                .annotate(count=Count('customer')).order_by('-count').first()['customer'])
            return customer
        else:
            return 'Current showroom doesn\'t have any customers'

    def last_month_income(self, obj):
        from django.db.models import Sum
        income = CustomerShowroomOffers.objects.filter(showroom=obj) \
                 .filter(offer_date__gt=datetime.datetime.now()-datetime.timedelta(days=31)) \
                 .aggregate(Sum('price'))['price__sum']
        return income

admin.site.register(CustomerShowroomOffers)
admin.site.register(CarPriceRelationShowroom)
