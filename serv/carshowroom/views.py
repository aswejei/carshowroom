from rest_framework.views import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from carshowroom.models import CarShowroom, CarPriceRelationShowroom
from carshowroom.serializers import CarShowroomSerializer, CarPriceRelationShowroomSerializer
from core.mixins import SafeDeleteModelMixin


class CarShowroomViewSet(SafeDeleteModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = CarShowroom.objects.filter(is_active=True)
    serializer_class = CarShowroomSerializer


class CarPriceRelationShowroomViewSet(SafeDeleteModelMixin,
                                      mixins.ListModelMixin,
                                      mixins.RetrieveModelMixin,
                                      mixins.CreateModelMixin,
                                      mixins.UpdateModelMixin,
                                      GenericViewSet):
    queryset = CarPriceRelationShowroom.objects.filter(is_active=True)
    serializer_class = CarPriceRelationShowroomSerializer
