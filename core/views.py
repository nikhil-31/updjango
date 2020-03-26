import structlog
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Merchant, Store, Item, Order
from .seralizers import MerchantSerializer, StoreSerializer, ItemsSerializer, OrderSerializer
from .tasks import save_orders

logger = structlog.getLogger(__name__)


class MerchantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    def get_queryset(self):
        queryset = Merchant.objects.all()
        queryset = queryset.select_related('owner')
        return queryset


class StoreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        queryset = queryset.select_related('merchant')
        return queryset


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        queryset = queryset.select_related('merchant')
        return queryset


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            # Saving orders in the bg using celery
            save_orders.delay(request.data)
            logger.info("order_saved", payload=request.data)
            return Response({"message": "Order Queued"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Order.objects.all()
        queryset = queryset.select_related('merchant')
        queryset = queryset.select_related('store')
        queryset = queryset.prefetch_related('items')
        return queryset
