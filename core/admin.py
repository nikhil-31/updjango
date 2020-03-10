from django.contrib import admin
from .models import Merchant, Stores, Items


# Register your models here.
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')


class StoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'lat', 'lng', 'merchant')


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'merchant')


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Stores, StoresAdmin)
admin.site.register(Items, ItemsAdmin)
