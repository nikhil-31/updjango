from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import MerchantView, StoresView, ItemsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/merchants/', MerchantView.as_view(), name='merchant-list'),
    path('api/stores/', StoresView.as_view(), name='stores-list'),
    path('api/items/', ItemsView.as_view(), name='items-list'),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
