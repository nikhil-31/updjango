from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from .models import Merchant, Store, Item, Order
from .seralizers import MerchantSerializer, StoreSerializer, ItemsSerializer, OrderSerializer
from .tasks import save_orders


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
            serializer = StoreSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            try:
                store = Store.objects.get(pk=pk)
            except Store.DoesNotExist:
                return Response(status=HTTP_400_BAD_REQUEST)
            serializer = StoreSerializer(store)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Store saved"}, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk, *args, **kwargs):
        store = Store.objects.get(pk=pk)
        serializer = StoreSerializer(store, data=request.data)
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


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        if pk is None:
            queryset = Order.objects.all()
            serializer = OrderSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            try:
                order = Order.objects.get(pk=pk)
            except Order.DoesNotExist:
                return Response(status=HTTP_400_BAD_REQUEST)
            serializer = OrderSerializer(order)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            # Saving orders in the bg using celery
            save_orders(request.data)
            return Response({"message": "Order Queued"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
