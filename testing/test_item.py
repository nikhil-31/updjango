import pytest
from django.urls import reverse
from .test_model_fixtures import *


def test_item_get_request(api_client, user, item):
    url = reverse('item-list')
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {}


def test_item_post_request(api_client, user, merchant):
    url = reverse('item-list')
    data = {
        "name": "Test Item",
        "price": "33.5",
        "description": "Test description",
        "merchant": {
            "id": merchant.id,
            "name": merchant.name,
            "owner": merchant.owner.id
        }
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201


def test_item_detail_request(api_client, user, merchant, item):
    url = reverse('item-detail', args=(item.id,))
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {
    #     'description': 'This is a test description',
    #     'id': 3,
    #     'merchant':
    #         {
    #             'id': 3,
    #             'name': 'Test merchant',
    #             'owner': 3
    #         },
    #     'name': 'Test item',
    #     'price': '255'
    # }


def test_item_put_request(api_client, user, merchant, item):
    url = reverse('item-detail', args=(item.id,))
    data = {
        "name": "Updated Item",
        "price": "33.5",
        "description": "Updated Test description",
        "merchant": {
            "id": merchant.id,
            "name": merchant.name,
            "owner": merchant.owner.id
        }
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    # assert response.json() == {}


def test_item_delete_request(api_client, user, merchant, item):
    url = reverse('item-detail', args=(item.id,))
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == 204
