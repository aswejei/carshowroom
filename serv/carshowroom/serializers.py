from rest_framework import serializers

from carshowroom.models import CarShowroom, CarPriceRelationShowroom, CustomerShowroomOffers


class CarShowroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarShowroom
        fields = ['name', 'location', 'car_characteristics', 'description', 'cars']


class CarPriceRelationShowroomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarPriceRelationShowroom
        fields = ['quantity', 'showroom', 'car', 'price']


class CustomerShowroomOffersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomerShowroomOffers
        fields = ['customer', 'showroom', 'car', 'price', 'offer_date']
