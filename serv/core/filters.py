from django_filters import rest_framework as filters

from serv.supplier.models import Car
from serv.carshowroom.models import CarPriceRelationShowroom, CarShowroom


class CarPriceRelationFilter(filters.FilterSet):
    price = filters.NumberFilter()
    price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')

    car__brand = filters.CharFilter(lookup_expr='icontains')
    car__color = filters.CharFilter(lookup_expr='icontains')
    car__car_body = filters.CharFilter(lookup_expr='icontains')


class CarPriceRelationShowroomFilter(CarPriceRelationFilter):
    showroom__name = filters.CharFilter(lookup_expr='icontains')
    showroom__location = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CarPriceRelationShowroom
        fields = [
            'price',
            'car__brand',
            'car__color',
            'car__car_body',
            'showroom__name',
            'showroom__location'
        ]


class CarPriceRelationSupplierFilter(CarPriceRelationFilter):
    supplier__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CarPriceRelationShowroom
        fields = [
            'price',
            'car__brand',
            'car__color',
            'car__car_body',
            'supplier__name'
        ]


class CarShowroomFilter(filters.FilterSet):
    class Meta:
        model = CarShowroom
        fields = [
            'name',
            'location',
        ]


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    date_founded = filters.DateFilter()
    date_founded__gt = filters.DateFilter(field_name='date_founded', lookup_expr='date__gt')
    date_founded__lt = filters.DateFilter(field_name='date_founded', lookup_expr='date__lt')


class CarFilter(filters.FilterSet):
    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'color'
        ]