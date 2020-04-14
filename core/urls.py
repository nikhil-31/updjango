from django.urls import path, include
from core.views import MerchantViewSet, StoreViewSet, ItemViewSet, OrderViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('merchants', MerchantViewSet, basename="merchant")
router.register('stores', StoreViewSet, basename="store")
router.register('items', ItemViewSet, basename="item")
router.register('orders', OrderViewSet, basename="order")

urlpatterns = [
    path('api/', include(router.urls)),
]
