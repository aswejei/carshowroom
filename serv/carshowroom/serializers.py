from abc import ABC

from rest_framework import serializers

from serv.core.inner_serializers import CarPriceRelationShowroomSerializerGetNoShowroomField
from serv.carshowroom.models import CarShowroom, CarPriceRelationShowroom, CustomerShowroomOffers
from serv.core.validators import is_car_characteristics_valid, is_balance_positive, is_price_positive


class CarShowroomSerializerGet(serializers.ModelSerializer):
    cars = CarPriceRelationShowroomSerializerGetNoShowroomField(many=True)

    class Meta:
        model = CarShowroom
        fields = [
            'name',
            'location',
            'car_characteristics',
            'description',
            'cars'
        ]


class CarShowroomSerializerPost(serializers.ModelSerializer):
    car_characteristics = serializers.JSONField(validators=[is_car_characteristics_valid])
    balance = serializers.FloatField(validators=[is_balance_positive])

    class Meta:
        model = CarShowroom
        fields = [
            'name',
            'location',
            'car_characteristics',
            'description',
            'balance'
        ]


class CarPriceRelationShowroomSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = CarPriceRelationShowroom
        depth = 1
        fields = [
            'quantity',
            'showroom',
            'car',
            'price'
        ]


class CarPriceRelationShowroomSerializerPost(serializers.ModelSerializer):
    car_id = serializers.IntegerField(read_only=False)
    showroom_id = serializers.IntegerField(read_only=False)
    price = serializers.FloatField(validators=[is_price_positive])

    class Meta:
        model = CarPriceRelationShowroom
        fields = [
            'quantity',
            'showroom_id',
            'car_id',
            'price'
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.filter(is_active=True),
                fields=('car_id', 'showroom_id'),
                message="You can not create car price record twice"
            )
        ]


class CustomerShowroomOffersSerializerPost(serializers.Serializer):
    max_price = serializers.FloatField()
    characteristics_dict = serializers.JSONField()


class CustomerShowroomOffersSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = CustomerShowroomOffers
        depth = 1
        fields = [
            'customer',
            'showroom',
            'car',
            'price',
            'offer_date'
        ]

