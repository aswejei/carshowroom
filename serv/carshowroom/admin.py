from django.contrib import admin

# Register your models here.
from carshowroom.models import CarShowroom, CustomerShowroomOffers, CarPriceRelationShowroom

admin.site.register(CarShowroom)
admin.site.register(CustomerShowroomOffers)
admin.site.register(CarPriceRelationShowroom)
