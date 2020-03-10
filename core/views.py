from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Merchant, Stores, Items
from .seralizers import MerchantSerializer, StoresSerializer, ItemsSerializer


class MerchantView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        queryset = Merchant.objects.all()
        serializer = MerchantSerializer(queryset, many=True)
        return Response(serializer.data)


class StoresView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        queryset = Stores.objects.all()
        serializer = StoresSerializer(queryset, many=True)
        return Response(serializer.data)


class ItemsView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        queryset = Items.objects.all()
        serializer = ItemsSerializer(queryset, many=True)
        return Response(serializer.data)