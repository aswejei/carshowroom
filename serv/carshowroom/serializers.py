from rest_framework import serializers

from carshowroom.models import CarShowroom, CarPriceRelationShowroom, CustomerShowroomOffers
from supplier.serializers import CarPriceRelationSerializer, CarSerializer


class CarShowroomSerializer(serializers.ModelSerializer):
    car_prices = CarPriceRelationSerializer(many=True)

    class Meta:
        model = CarShowroom
        fields = ['name', 'location', 'car_characteristics', 'description', 'car_prices']


class CarPriceRelationShowroomSerializer(serializers.ModelSerializer):
    showroom = CarShowroomSerializer()
    car = CarSerializer()

    class Meta:
        model = CarPriceRelationShowroom
        fields = ['quantity', 'showroom', 'car', 'price']


class CustomerShowroomOffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerShowroomOffers
        fields = ['customer', 'showroom', 'car', 'price', 'offer_date']
