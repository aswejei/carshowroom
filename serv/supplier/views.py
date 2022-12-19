import rest_framework.filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from core.filters import SupplierFilter, CarFilter, CarPriceRelationSupplierFilter
from supplier.models import Car, CarPriceRelationSupplier, Supplier
from supplier.serializers import CarSerializer, SupplierSerializerGet ,SupplierSerializerPost, \
    CarPriceRelationSupplierSerializerPost, CarPriceRelationSupplierSerializerGet
from core.mixins import SafeDeleteModelMixin


class CarViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 SafeDeleteModelMixin,
                 GenericViewSet):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer
    filter_backends = [rest_framework.filters.SearchFilter, DjangoFilterBackend]
    filter_class = CarFilter
    search_fields = ['brand', 'model', 'color']


class CarPriceRelationSupplierViewSet(SafeDeleteModelMixin,
                                      mixins.ListModelMixin,
                                      mixins.RetrieveModelMixin,
                                      mixins.CreateModelMixin,
                                      mixins.UpdateModelMixin,
                                      GenericViewSet):
    queryset = CarPriceRelationSupplier.objects.filter(is_active=True)
    serializer_class_post = CarPriceRelationSupplierSerializerPost
    serializer_class_get = CarPriceRelationSupplierSerializerGet
    filter_backends = [rest_framework.filters.SearchFilter, DjangoFilterBackend]
    filter_class = CarPriceRelationSupplierFilter
    search_fields = ['car__brand', 'car__model', 'car__color', 'supplier__name']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        elif self.request.method == 'GET':
            return self.serializer_class_get
        else:
            return self.serializer_class_post


class SupplierViewSet(SafeDeleteModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      GenericViewSet):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class_post = SupplierSerializerPost
    serializer_class_get = SupplierSerializerGet
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    search_fields = ['name']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        elif self.request.method == 'GET':
            return self.serializer_class_get
        else:
            return self.serializer_class_post
