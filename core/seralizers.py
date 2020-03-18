from rest_framework import serializers
from .models import Merchant, Store, Item


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
