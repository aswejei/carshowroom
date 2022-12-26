from rest_framework import serializers

from serv.core.validators import is_proper_percent
from serv.discount.models import CarShowroomDiscount, SupplierDiscount
from serv.supplier.serializers import CarPriceRelationSupplierSerializerGet
from serv.carshowroom.serializers import CarPriceRelationShowroomSerializerGet


class ShowroomDiscountSerializerGet(serializers.ModelSerializer):
    discounted_record = CarPriceRelationShowroomSerializerGet()

    class Meta:
        model = CarShowroomDiscount
        fields = [
            'discount',
            'discounted_record'
        ]
        depth = 1


class ShowroomDiscountSerializerPost(serializers.ModelSerializer):
    discount = serializers.FloatField(validators=[is_proper_percent])

    class Meta:
        model = CarShowroomDiscount
        fields = [
            'discount',
            'discounted_record'
        ]


class SupplierDiscountSerializerGet(serializers.ModelSerializer):
    discounted_record = CarPriceRelationSupplierSerializerGet()

    class Meta:
        model = SupplierDiscount
        fields = [
            'discount',
            'discounted_record'
        ]
        depth = 1


class SupplierDiscountSerializerPost(serializers.ModelSerializer):
    discount = serializers.FloatField(validators=[is_proper_percent])

    class Meta:
        model = SupplierDiscount
        fields = [
            'discount',
            'discounted_record'
        ]
