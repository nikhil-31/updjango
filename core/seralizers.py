from rest_framework import serializers
from .models import Merchant, Stores, Items


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = ('name', 'owner')


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stores
        fields = '__all__'


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = '__all__'
