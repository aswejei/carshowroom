from rest_framework import serializers

from supplier.models import Supplier, Car, ShowroomSupplierOffers, CarPriceRelationSupplier


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['brand',
                  'model',
                  'color',
                  'engine_v',
                  'car_body',
                  'id']


class CarPriceRelationSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=False)
    price = serializers.IntegerField()

    class Meta:
        model = CarPriceRelationSupplier
        fields = ['car',
                  'price',
                  'id']


class SupplierSerializer(serializers.ModelSerializer):
    car_prices = CarPriceRelationSerializer(many=True)
    date_founded = serializers.DateField()

    class Meta:
        model = Supplier
        fields = ['name',
                  'date_founded',
                  'description',
                  'car_prices',
                  'id']


class CarPriceRelationSupplierSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=False)
    supplier = SupplierSerializer(many=False,
                                  context={'exclude_fields': ['car_prices']})
    price = serializers.IntegerField()

    class Meta:
        model = CarPriceRelationSupplier
        fields = ['car',
                  'price',
                  'supplier',
                  'id']


class ShowroomSupplierOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowroomSupplierOffers
        fields = ['car',
                  'showroom',
                  'supplier',
                  'price',
                  'date']
