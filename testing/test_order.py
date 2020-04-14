import pytest
from django.urls import reverse
from .test_model_fixtures import *


def test_order_get_request(api_client, user, order):
    url = reverse('order-list')
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {}


def test_order_detail_request(api_client, user, order):
    url = reverse('order-detail', args=(order.id,))
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {}


def test_order_post_request(api_client, user, store, merchant, item):
    url = reverse('order-list')
    api_client.force_authenticate(user=user)
    data = {
        "address": "Nallurhalli",
        "merchant": {
            "id": merchant.id,
            "name": merchant.name,
            "owner": merchant.owner.id
        },
        "store": {
            "id": 1,
            "name": store.name,
            "address": store.address,
            "lat": store.lat,
            "lng": store.lng,
            "merchant": {
                "id": merchant.id,
                "name": merchant.name,
                "owner": merchant.owner.id
            }
        },
        "items": [
            {
                "id": item.id,
                "name": item.name,
                "price": item.price,
                "description": item.description,
                "merchant": {
                    "id": merchant.id,
                    "name": merchant.name,
                    "owner": merchant.owner.id
                }
            }
        ],
        "order_subtotal": 240.0,
        "taxes": 10.0,
        "order_total": 250.0
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == 200
    assert response.json() == {'message': 'Order Queued'}
