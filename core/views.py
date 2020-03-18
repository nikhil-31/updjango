from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from .models import Merchant, Store, Item
from .seralizers import MerchantSerializer, StoresSerializer, ItemsSerializer


class MerchantView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            queryset = Merchant.objects.all()
            serializer = MerchantSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            try:
                merchant = Merchant.objects.get(pk=pk)
            except Merchant.DoesNotExist:
                return Response(status=HTTP_400_BAD_REQUEST)
            serializer = MerchantSerializer(merchant)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = MerchantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "merchant saved"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        mc = Merchant.objects.get(pk=pk)
        items = Item.objects.filter(merchant=mc)
        serializer = MerchantSerializer(mc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        merchant = Merchant.objects.get(pk=pk)
        merchant.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class StoresView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            queryset = Store.objects.all()
            serializer = StoresSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            try:
                store = Store.objects.get(pk=pk)
            except Store.DoesNotExist:
                return Response(status=HTTP_400_BAD_REQUEST)
            serializer = StoresSerializer(store)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Store saved"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        store = Store.objects.get(pk=pk)
        serializer = StoresSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        store = Store.objects.get(pk=pk)
        store.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class ItemsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            queryset = Item.objects.all()
            serializer = ItemsSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            try:
                item = Item.objects.get(pk=pk)
            except Item.DoesNotExist:
                return Response(status=HTTP_400_BAD_REQUEST)
            serializer = ItemsSerializer(item)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Item saved"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        serializer = ItemsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        item = Item.objects.get(pk=pk)
        item.delete()
        return Response(status=HTTP_204_NO_CONTENT)
