from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView

from carshowroom.models import CustomerShowroomOffers
from core.operations import parse_dict_to_Q_expr


# Create your views here.


class ShowroomStats(APIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self, request: Request):
        return CustomerShowroomOffers.objects.filter(parse_dict_to_Q_expr(request.query_params))

    def get(self, request, format=None):
        self.get_queryset(request)


class SupplierStats(APIView):
    pass
