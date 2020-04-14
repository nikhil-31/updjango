import pytest
from django.urls import reverse
from .test_model_fixtures import *


def test_store_get_request(api_client, user, store):
    url = reverse('store-list')
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {
    #     'count': 1,
    #     'next': None,
    #     'previous': None,
    #     'results': [
    #         {
    #             'address': 'test address',
    #             'id': 5,
    #             'lat': 1.5,
    #             'lng': 2.5,
    #             'merchant': {'id': 11, 'name': 'Test merchant', 'owner': 11},
    #             'name': 'Store test'
    #         }
    #     ]
    # }


def test_store_detail_request(api_client, user, store):
    url = reverse('store-detail', args=(store.id,))
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {
    #     'address': 'test address',
    #     'id': 6,
    #     'lat': 1.5,
    #     'lng': 2.5,
    #     'merchant': {
    #         'id': 12, 'name': 'Test merchant', 'owner': 12
    #     },
    #     'name': 'Store test'
    # }


def test_store_post_request(api_client, user, merchant):
    url = reverse('store-list')
    data = {
        "name": "Test name",
        "address": "Test Address",
        "lat": 1.0000,
        "lng": 1.0000,
        "merchant": {
            "id": merchant.id,
            "name": merchant.name,
            "owner": merchant.owner.id
        }
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.json() == {
        'address': 'Test Address',
        'lat': 1.0,
        'lng': 1.0,
        'merchant': {
            "id": merchant.id,
            "name": merchant.name,
            "owner": merchant.owner.id
        },
        'name': 'Test name'
    }


def test_store_put_request(api_client, user, store, merchant):
    url = reverse('store-detail', args=(store.id,))
    data = {
        "name": "Updated Test name",
        "address": "Updated Test Address",
        "lat": 2.0000,
        "lng": 2.0000,
        "merchant": {
            "id": merchant.id,
            "name": merchant.name,
            "owner": merchant.owner.id
        }
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200


def test_store_delete_request(api_client, user, store):
    url = reverse('store-detail', args=(store.id,))
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == 204
