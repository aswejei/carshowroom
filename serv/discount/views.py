from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from core.mixins import SafeDeleteModelMixin
from discount.models import SupplierDiscount, CarShowroomDiscount
from discount.serializers import SupplierDiscountSerializerPost, SupplierDiscountSerializerGet, \
    ShowroomDiscountSerializerPost, ShowroomDiscountSerializerGet


class SupplierDiscountViewSet(SafeDeleteModelMixin,
                              ListModelMixin,
                              RetrieveModelMixin,
                              CreateModelMixin,
                              UpdateModelMixin,
                              GenericViewSet):
    queryset = SupplierDiscount.objects.prefetch_related('discounted_record__supplier',
                                                         'discounted_record__car').filter(is_active=True)
    serializer_class_post = SupplierDiscountSerializerPost
    serializer_class_get = SupplierDiscountSerializerGet

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        elif self.request.method == 'GET':
            return self.serializer_class_get
        else:
            return self.serializer_class_post


class ShowroomDiscountViewSet(SafeDeleteModelMixin,
                              ListModelMixin,
                              RetrieveModelMixin,
                              CreateModelMixin,
                              UpdateModelMixin,
                              GenericViewSet):
    queryset = CarShowroomDiscount.objects.prefetch_related('discounted_record__showroom',
                                                            'discounted_record__car').filter(is_active=True)
    serializer_class_post = ShowroomDiscountSerializerPost
    serializer_class_get = ShowroomDiscountSerializerGet

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return self.serializer_class_post
        elif self.request.method == 'GET':
            return self.serializer_class_get
        else:
            return self.serializer_class_post
