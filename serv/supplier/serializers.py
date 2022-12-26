from rest_framework import serializers

from serv.core.validators import is_price_positive
from serv.supplier.models import Supplier, Car, ShowroomSupplierOffers, CarPriceRelationSupplier


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'brand',
            'model',
            'color',
            'engine_v',
            'car_body',
            'id'
        ]


class CarPriceRelationSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=False)
    price = serializers.IntegerField(validators=[is_price_positive])

    class Meta:
        model = CarPriceRelationSupplier
        fields = [
            'car',
            'price',
            'id',
        ]


class SupplierSerializerGet(serializers.ModelSerializer):
    cars = CarPriceRelationSerializer(many=True)

    class Meta:
        model = Supplier
        fields = [
            'name',
            'date_founded',
            'description',
            'cars',
            'id'
        ]
        depth = 1


class SupplierSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'name',
            'date_founded',
            'description',
            'id'
        ]


class CarPriceRelationSupplierSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = CarPriceRelationSupplier
        fields = [
            'car',
            'supplier',
            'price',
            'price_with_discount',
            'id'
        ]
        depth = 1


class CarPriceRelationSupplierSerializerPost(serializers.ModelSerializer):
    price = serializers.FloatField(validators=[is_price_positive])

    class Meta:
        model = CarPriceRelationSupplier
        fields = [
            'car',
            'price',
            'supplier',
            'id'
        ]
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.filter(is_active=True),
                fields=('car_id', 'supplier_id'),
                message="You can not create car-price record twice"
            )
        ]


class ShowroomSupplierOffersSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = ShowroomSupplierOffers
        fields = [
            'car',
            'showroom',
            'supplier',
            'price',
            'date'
        ]
        depth = 1


class ShowroomSupplierOffersSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = ShowroomSupplierOffers
        fields = [
            'car',
            'showroom',
            'supplier',
            'price',
            'date'
        ]
