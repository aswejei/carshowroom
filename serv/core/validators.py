from typing import Dict

from rest_framework import serializers

from serv.supplier.models import Car


def is_proper_percent(value: float):
    if value > 0 or value < 100:
        raise serializers.ValidationError("Given discount must be greater than 0 and less than 100")


def is_car_characteristics_valid(json_dict: Dict):
    key_set = set(json_dict.keys())
    fields_set = {i.name for i in Car._meta.local_fields}
    if not fields_set.issuperset(key_set):
        raise serializers.ValidationError("Json string fields are invalid")


def is_price_positive(value: float):
    if value < 0:
        raise serializers.ValidationError("Price must be positive number")


def is_balance_positive(value: float):
    if value < 0:
        raise serializers.ValidationError("Balance must be positive number")
