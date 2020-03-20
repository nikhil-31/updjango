from django.urls import path
from core.views import MerchantView, StoresView, ItemsView, OrderView

urlpatterns = [
    path('api/merchants/', MerchantView.as_view(), name='merchant-list'),
    path('api/merchants/<int:pk>/', MerchantView.as_view(), name='merchant-detail'),
    path('api/stores/', StoresView.as_view(), name='stores-list'),
    path('api/stores/<int:pk>/', StoresView.as_view(), name='stores-detail'),
    path('api/items/', ItemsView.as_view(), name='items-list'),
    path('api/items/<int:pk>/', ItemsView.as_view(), name='items-detail'),
    path('api/orders/', OrderView.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderView.as_view(), name='order-detail')
]
