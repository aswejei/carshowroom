from rest_framework import serializers

from supplier.models import Supplier, Car, ShowroomSupplierOffers, CarPriceRelationSupplier


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Supplier
        fields = ['name', 'date_founded', 'description', 'cars']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'color', 'engine_v', 'car_body']


class CarPriceRelationSupplierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarPriceRelationSupplier
        fields = ['car', 'price', 'supplier']


class ShowroomSupplierOffersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowroomSupplierOffers
        fields = ['car', 'showroom', 'supplier', 'price', 'date']

