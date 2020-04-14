import pytest
from core.models import Merchant, Store, Item, Order
from django.contrib.auth.models import User
import uuid


@pytest.fixture()
def user(db):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    return user


@pytest.fixture()
def test_password():
    return 'strong-test-pass'


@pytest.fixture()
def create_user(db, django_user_model, test_password):
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)

    return make_user


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
def api_client_with_credentials(db, create_user, api_client):
    user = create_user()
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)


@pytest.fixture()
def merchant(db, user):
    merchant = Merchant.objects.create(name="Test merchant", owner=user)
    return merchant


@pytest.fixture()
def store(db, merchant):
    store = Store.objects.create(name="Store test", address="test address", lat=1.5, lng=2.5, merchant=merchant)
    return store


@pytest.fixture()
def item(db, store, merchant):
    item = Item.objects.create(name='Test item', price='255', description='This is a test description',
                               merchant=merchant)
    return item


@pytest.fixture()
def order(db, store, merchant, item):

    order = Order(address="This is the test address", merchant=merchant, store=store,
                  order_subtotal=123.23, taxes=452.24, order_total=234.12)
    order.save()

    item_list = [item.id]
    order.items.add(*item_list)
    return order
