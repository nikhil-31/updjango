from celery import shared_task
import structlog

from .models import Merchant, Store, Order, Item

logger = structlog.getLogger(__name__)


@shared_task
def print_random_task(total):
    for i in range(total):
        print(i)
    return '{} random numbers printed'.format(total)


@shared_task
def save_orders(validated_data):
    try:
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

        logger.info("Saving Order ", order_payload=validated_data, order_obj=str(order))
        return "Task completed successfully"
    except Exception as e:
        return str(e)
