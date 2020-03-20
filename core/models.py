from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models


def delivery_time():
    now = datetime.now()
    return now + timedelta(minutes=45)


# Merchant model, each merchant has an owner which is the user
class Merchant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


# Stores model, each store is related to a merchant
class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    lng = models.FloatField()
    merchant = models.ForeignKey(Merchant, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


# Items model, each item is related to a merchant
class Item(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default=None, blank=True)
    merchant = models.ForeignKey(Merchant, default=None, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.name


class Order(models.Model):
    address = models.CharField(max_length=1000)
    merchant = models.ForeignKey(Merchant, default=None, on_delete=models.SET_DEFAULT)
    store = models.ForeignKey(Store, default=None, on_delete=models.SET_DEFAULT)
    items = models.ManyToManyField(Item, related_name="order_items")
    order_subtotal = models.FloatField()
    taxes = models.FloatField()
    order_total = models.FloatField()
    created_time = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DateTimeField(default=delivery_time())
