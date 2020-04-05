from django.urls import path, include
from core.views import MerchantViewSet, StoreViewSet, ItemViewSet, OrderViewSet, ItemSearchViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('merchants', MerchantViewSet)
router.register('stores', StoreViewSet)
router.register('items', ItemViewSet)
router.register('orders', OrderViewSet)
router.register('searchitem', ItemSearchViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
