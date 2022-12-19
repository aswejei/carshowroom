import rest_framework.filters
from django_filters import rest_framework as filters
import json
from carshowroom.models import CarPriceRelationShowroom, CarShowroom
from supplier.models import Car


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
        fields = ['price', 'car__brand', 'car__color', 'car__car_body', 'showroom__name', 'showroom__location']


class CarPriceRelationSupplierFilter(CarPriceRelationFilter):
    supplier__name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CarPriceRelationShowroom
        fields = ['price', 'car__brand', 'car__color', 'car__car_body', 'supplier__name']


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


# class CarShowroomSearchFilter(rest_framework.filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         q = request.query_params.get('car_characteristics')
#         if q:
#             try:
#                 dec = json.JSONDecoder()
#                 query_dic = dec.decode(q)
#                 car_characteristics_query_params = []
#                 for i in query_dic:
#                     car_characteristics_query_params.append(f'{i}:{query_dic[i]}')
#                 request.query_params['car_characteristics'] = car_characteristics_query_params
#                 return request.query_params
#             except json.JSONDecodeError  as err:
#                 raise err
#         return super().get_search_fields(view, request)
