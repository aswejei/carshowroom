from django.contrib import admin

# Register your models here.
from supplier.models import Supplier, Car, CarPriceRelationSupplier, ShowroomSupplierOffers

admin.site.register(Supplier)
admin.site.register(Car)
admin.site.register(CarPriceRelationSupplier)
admin.site.register(ShowroomSupplierOffers)

