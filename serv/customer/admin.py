from django.contrib import admin

# Register your models here.
from serv.customer.models import Customer

admin.site.register(Customer)