from rest_framework import serializers

from carshowroom.models import CarPriceRelationShowroom
from supplier.models import CarPriceRelationSupplier
from supplier.serializers import CarSerializer


class CarPriceRelationShowroomSerializerGetNoShowroomField(serializers.ModelSerializer):
    class Meta:
        model = CarPriceRelationShowroom
        fields = [
            'quantity',
            'car',
            'price',
        ]
        depth = 1
