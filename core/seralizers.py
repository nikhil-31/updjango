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

    def validate(self, attrs):
        merchant_attr = attrs['merchant']
        merchant_id = merchant_attr['id']

        try:
            merchant = Merchant.objects.get(pk=merchant_id)
        except Merchant.DoesNotExist:
            raise serializers.ValidationError("Merchant does not exist")
        return attrs

    def create(self, validated_data):
        merchant_data = validated_data['merchant']
        merchant_id = merchant_data['id']
        merchant = Merchant.objects.get(pk=merchant_id)

        name = validated_data['name']
        address = validated_data['address']
        lat = validated_data['lat']
        lng = validated_data['lng']

        store = Store(merchant=merchant, name=name, address=address, lat=lat, lng=lng)
        store.save()

        return validated_data


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

    def validate(self, attrs):
        merchant_attr = attrs['merchant']
        merchant_id = merchant_attr['id']

        try:
            merchant = Merchant.objects.get(pk=merchant_id)
        except Merchant.DoesNotExist:
            raise serializers.ValidationError("Merchant does not exist")
        return attrs

    def create(self, validated_data):
        merchant_data = validated_data['merchant']
        merchant_id = merchant_data['id']
        merchant = Merchant.objects.get(pk=merchant_id)

        name = validated_data['name']
        price = validated_data['price']
        description = validated_data['description']

        item = Item(merchant=merchant, name=name, price=price, description=description)
        item.save()

        return validated_data


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

    def validate(self, attrs):
        print(attrs)

        store_attr = attrs['store']
        merchant_attr = attrs['merchant']
        items_attr = attrs['items']

        store_id = store_attr['id']
        merchant_id = merchant_attr['id']

        address = attrs['address']
        order_subtotal = attrs['order_subtotal']
        taxes = attrs['taxes']
        order_total = attrs['order_total']

        try:
            merchant = Merchant.objects.get(pk=merchant_id)
        except Merchant.DoesNotExist:
            raise serializers.ValidationError("Merchant does not exist")

        try:
            store = Store.objects.get(pk=store_id)
        except Store.DoesNotExist:
            raise serializers.ValidationError("Store does not exist")

        for item in items_attr:
            try:
                item = Item.objects.get(pk=item['id'])
            except Item.DoesNotExist:
                raise serializers.ValidationError("Invalid items passed")

            if merchant != item.merchant:
                raise serializers.ValidationError(f"{item.name} not associated with merchant")

        if merchant != store.merchant:
            raise serializers.ValidationError("Store is not associated with the merchant")

        return attrs

    # def create(self, validated_data):
    #     store = validated_data.pop('store')
    #     items = validated_data.pop('items')
    #     merchant = validated_data.pop('merchant')
    #     address = validated_data['address']
    #     order_subtotal = validated_data['order_subtotal']
    #     taxes = validated_data['taxes']
    #     order_total = validated_data['order_total']
    #
    #     merchant_model = Merchant.objects.get(pk=merchant['id'])
    #     store_model = Store.objects.get(pk=store['id'])
    #
    #     order = Order(address=address, merchant=merchant_model, store=store_model, order_subtotal=order_subtotal,
    #                   taxes=taxes, order_total=order_total)
    #     order.save()
    #
    #     for item in items:
    #         order.items.add(item['id'])
    #         print(item['id'])
    #
    #     return validated_data
