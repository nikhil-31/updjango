from django.urls import path, include
from core.views import MerchantViewSet, StoreViewSet, ItemViewSet, OrderViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('merchants', MerchantViewSet)
router.register('stores', StoreViewSet)
router.register('items', ItemViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
