import rest_framework.filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from serv.carshowroom.models import CarShowroom, CarPriceRelationShowroom, CustomerShowroomOffers
from serv.carshowroom.serializers import CarPriceRelationShowroomSerializerPost, \
    CarPriceRelationShowroomSerializerGet, CarShowroomSerializerGet, CarShowroomSerializerPost, \
    CustomerShowroomOffersSerializerGet, CustomerShowroomOffersSerializerPost
from serv.carshowroom.tasks import generate_offer
from serv.core.filters import CarPriceRelationShowroomFilter, CarShowroomFilter
from serv.core.mixins import SafeDeleteModelMixin, OfferCreateModelMixin


class CarShowroomViewSet(SafeDeleteModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         GenericViewSet):
    queryset = CarShowroom.objects.filter(is_active=True).prefetch_related('cars')
    serializer_class_post = CarShowroomSerializerPost
    serializer_class_get = CarShowroomSerializerGet
    filter_backends = [
        DjangoFilterBackend,
        rest_framework.filters.SearchFilter
    ]
    filterset_class = CarShowroomFilter
    search_fields = [
        'name',
        'location'
    ]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        elif self.request.method == 'GET':
            return self.serializer_class_get
        else:
            return self.serializer_class_post


class CarPriceRelationShowroomViewSet(SafeDeleteModelMixin,
                                      mixins.ListModelMixin,
                                      mixins.RetrieveModelMixin,
                                      mixins.CreateModelMixin,
                                      mixins.UpdateModelMixin,
                                      GenericViewSet):
    queryset = CarPriceRelationShowroom.objects.select_related('showroom', 'car').filter(is_active=True)
    serializer_class_post = CarPriceRelationShowroomSerializerPost
    serializer_class_get = CarPriceRelationShowroomSerializerGet
    filter_backends = [
        DjangoFilterBackend,
        rest_framework.filters.SearchFilter
    ]
    filterset_class = CarPriceRelationShowroomFilter
    search_fields = [
        'car__brand',
        'car__model',
        'car__color',
        'showroom__name',
    ]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        elif self.request.method == 'GET':
            return self.serializer_class_get
        else:
            return self.serializer_class_post


class CustomerShowroomOfferViewSet(SafeDeleteModelMixin,
                                   OfferCreateModelMixin,
                                   mixins.ListModelMixin,
                                   mixins.RetrieveModelMixin,
                                   GenericViewSet):
    serializer_class_get = CustomerShowroomOffersSerializerGet
    serializer_class_post = CustomerShowroomOffersSerializerPost
    permission_classes = [IsAuthenticated]
    order_generator = generate_offer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        else:
            return self.serializer_class_get

    def get_order_generator(self):
        return self.order_generator

    def get_queryset(self):
        queryset = CustomerShowroomOffers.objects.select_related('customer', 'showroom', 'car').filter(
            customer__user=self.request.user.id)
        return queryset
