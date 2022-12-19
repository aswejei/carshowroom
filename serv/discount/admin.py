from django.contrib import admin

# Register your models here.
from discount.models import SupplierDiscount, CarShowroomDiscount

admin.site.register(SupplierDiscount)
admin.site.register(CarShowroomDiscount)
