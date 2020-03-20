from rest_framework import serializers
from .models import Merchant, Store, Item, Order


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = (
            "id",
            "name",
            "owner"
        )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class StoreSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer()

    class Meta:
        model = Store
        fields = (
            "id",
            "name",
            "address",
            "lat",
            "lng",
            "merchant"
        )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class ItemsSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer()

    class Meta:
        model = Item
        fields = (
            "id",
            "name",
            "price",
            "description",
            "merchant"
        )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }


class OrderSerializer(serializers.ModelSerializer):
    store = StoreSerializer()
    items = ItemsSerializer(many=True)
    merchant = MerchantSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "address",
            "merchant",
            "store",
            "items",
            "order_subtotal",
            "taxes",
            "order_total",
            "created_time",
            "delivery_time",
        )

    def create(self, validated_data):
        print(validated_data)

        store = validated_data.pop('store')
        items = validated_data.pop('items')
        merchant = validated_data.pop('merchant')
        address = validated_data['address']
        order_subtotal = validated_data['order_subtotal']
        taxes = validated_data['taxes']
        order_total = validated_data['order_total']

        merchant_model = Merchant.objects.get(pk=merchant['id'])
        store_model = Store.objects.get(pk=store['id'])

        order = Order(address=address, merchant=merchant_model, store=store_model, order_subtotal=order_subtotal,
                      taxes=taxes, order_total=order_total)
        order.save()

        for item in items:
            order.items.add(item['id'])
            print(item['id'])

        return validated_data
