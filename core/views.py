import structlog
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from .models import Merchant, Store, Item, Order
from .seralizers import MerchantSerializer, StoreSerializer, ItemsSerializer, OrderSerializer
from .tasks import save_orders

structlog.configure(processors=[structlog.processors.JSONRenderer()])
logger = structlog.getLogger(__name__)


class MerchantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    def get_queryset(self):
        queryset = Merchant.objects.get_queryset().order_by('id')
        queryset = queryset.select_related('owner')
        return queryset

    def create(self, request, *args, **kwargs):
        resp = super(MerchantViewSet, self).create(request)
        logger.msg("merchant_created", payload=request.data)
        return resp


class StoreViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def get_queryset(self):
        queryset = Store.objects.get_queryset().order_by('id')
        queryset = queryset.select_related('merchant')
        return queryset

    def create(self, request, *args, **kwargs):
        resp = super(StoreViewSet, self).create(request)
        logger.msg("store_created", payload=request.data)
        return resp


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemsSerializer

    def get_queryset(self):
        if self.request.query_params.get('merchant_id') is not None:
            merchant_id = self.request.query_params.get('merchant_id')
            queryset = Item.objects.filter(merchant=merchant_id).order_by('id')
            return queryset
        elif self.request.query_params.get('q') is not None:
            name = self.request.query_params.get('q')
            queryset = Item.objects.filter(name__icontains=name).order_by('id')
            return queryset
        else:
            queryset = Item.objects.get_queryset().order_by('id')
            queryset = queryset.select_related('merchant')
            return queryset

    def create(self, request, *args, **kwargs):
        resp = super(ItemViewSet, self).create(request)
        logger.msg("item_created", payload=request.data)
        return resp


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            save_orders.delay(request.data)
            # save_orders.apply_async(args=[request.data], countdown=5)
            logger.msg("order_created", payload=request.data)
            return Response({"message": "Order Queued"})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    # def get_queryset(self):
    #     queryset = Order.objects.get_queryset().order_by('id')
    #     queryset = queryset.select_related('merchant')
    #     queryset = queryset.select_related('store')
    #     queryset = queryset.prefetch_related('items')
    #     return queryset
