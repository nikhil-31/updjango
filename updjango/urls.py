from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import merchant_list, merchant_detail, stores_list, stores_detail, items_list, items_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/merchants/', MerchantView.as_view(), name='merchant-list'),
    # path('api/stores/', StoresView.as_view(), name='stores-list'),
    # path('api/items/', ItemsView.as_view(), name='items-list'),
    path('api/merchants/', merchant_list, name='merchant-list'),
    path('api/merchants/<int:pk>', merchant_detail, name='merchant-detail'),
    path('api/stores/', stores_list, name='stores-list'),
    path('api/stores/<int:pk>', stores_detail, name='stores-detail'),
    path('api/items/', items_list, name='items-list'),
    path('api/items/<int:pk>', items_detail, name='items-detail'),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
