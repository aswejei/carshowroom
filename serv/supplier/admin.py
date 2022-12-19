import datetime

from django.contrib import admin

from serv.carshowroom.models import CarShowroom
from serv.supplier.models import Supplier, Car, CarPriceRelationSupplier, ShowroomSupplierOffers


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_founded', 'amount_of_sold_cars', 'top_showroom', 'last_month_income']

    def amount_of_sold_cars(self, obj):
        result = ShowroomSupplierOffers.objects.filter(supplier=obj).count()
        return result

    def top_showroom(self, obj):
        from django.db.models import Count
        if ShowroomSupplierOffers.objects.filter(supplier=obj).first():
            showroom = CarShowroom.objects.get(id=ShowroomSupplierOffers.objects.filter(supplier=obj).values('showroom') \
                                            .annotate(count=Count('showroom')).order_by('-count').first()['showroom'])
            return showroom
        else:
            return 'Current supplier doesn\'t have any clients'

    def last_month_income(self, obj):
        from django.db.models import Sum
        income = ShowroomSupplierOffers.objects.filter(supplier=obj) \
            .filter(date__gt=datetime.datetime.now()-datetime.timedelta(days=31)) \
            .aggregate(Sum('price'))['price__sum']
        return income


admin.site.register(Car)
admin.site.register(CarPriceRelationSupplier)
admin.site.register(ShowroomSupplierOffers)
