from django.db import models
from django.contrib.auth.models import User


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
