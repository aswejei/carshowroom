import django.db.models
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.mixins import DestroyModelMixin


class SafeDeleteModelMixin:
    @action(methods=['delete'], detail=True)
    def safe_delete(self, request, pk=None):
        instance = self.queryset.get(pk=pk)
        instance.safe_delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#
# class SafeDeleteModelMixin(DestroyModelMixin):
#     def perform_destroy(self, instance):
#         instance.is_active = False
#         instance.save()
#         for obj in instance.related_objects:
#             obj.is_active = False
#             obj.save()
        # for field in instance.__class__._meta.fields:
        #     if field.is_relation:
        #         field.related_model.is_active = False
        #         field.related_model.save()

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
