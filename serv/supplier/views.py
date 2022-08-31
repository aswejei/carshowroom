from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from supplier.models import Car, CarPriceRelationSupplier, Supplier
from supplier.serializers import CarSerializer, CarPriceRelationSupplierSerializer, SupplierSerializer
from core.mixins import SafeDeleteModelMixin


class CarViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 SafeDeleteModelMixin,
                 GenericViewSet):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer


class CarPriceRelationSupplierViewSet(SafeDeleteModelMixin,
                                      mixins.ListModelMixin,
                                      mixins.RetrieveModelMixin,
                                      mixins.CreateModelMixin,
                                      mixins.UpdateModelMixin,
                                      GenericViewSet):
    queryset = CarPriceRelationSupplier.objects.filter(is_active=True)
    serializer_class = CarPriceRelationSupplierSerializer


class SupplierViewSet(SafeDeleteModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = SupplierSerializer
