from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from serv.core.mixins import SafeDeleteModelMixin
from serv.customer.models import Customer
from serv.customer.serializers import CustomerSerializer


class CustomerViewSet(
                      SafeDeleteModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      GenericViewSet
                     ):
    queryset = Customer.objects.filter(is_active=True)
    serializer_class = CustomerSerializer

