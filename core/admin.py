from django.contrib import admin
from .models import Merchant, Store, Item, Order


# Register your models here.
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


class StoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'lat', 'lng', 'merchant')


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'merchant')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_total')


admin.site.register(Order, OrderAdmin)
admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Store, StoresAdmin)
admin.site.register(Item, ItemsAdmin)
