from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import mixins


class SafeDeleteModelMixin:
    @action(methods=['delete'], detail=True)
    def safe_delete(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.safe_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OfferCreateModelMixin(mixins.CreateModelMixin):
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order_generator = self.get_order_generator()
        order = order_generator(**serializer.data, request=request)
        serializer = self.serializer_class_get(order)
        serializer.is_valid()
        headers = self.get_success_headers(serializer.data)
        if order:
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)