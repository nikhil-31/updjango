from django.contrib import admin
from .models import Merchant, Stores, Items


# Register your models here.
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name')


class StoresAdmin(admin.ModelAdmin):
    list_display = ('merchant', 'name', 'address', 'lat', 'lng')


class ItemsAdmin(admin.ModelAdmin):
    list_display = ('merchant', 'name', 'price', 'description')


admin.site.register(Merchant, MerchantAdmin)
admin.site.register(Stores, StoresAdmin)
admin.site.register(Items, ItemsAdmin)
