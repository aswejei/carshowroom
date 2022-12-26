from rest_framework import serializers

from serv.carshowroom.models import CarPriceRelationShowroom


class CarPriceRelationShowroomSerializerGetNoShowroomField(serializers.ModelSerializer):
    class Meta:
        model = CarPriceRelationShowroom
        fields = [
            'quantity',
            'car',
            'price',
        ]
        depth = 1
