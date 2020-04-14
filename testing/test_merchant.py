import pytest
from django.urls import reverse
from .test_model_fixtures import *
from core.seralizers import MerchantSerializer
from core.models import Merchant


def test_merchant_get_request(api_client, user, merchant):
    url = reverse('merchant-list')
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    # assert response.json() == {
    #     'count': 1,
    #     'next': None,
    #     'previous': None,
    #     'results': [
    #         {
    #             'id': 1,
    #             'name': 'Test merchant',
    #             'owner': user.id
    #         }
    #     ]
    # }


def test_merchant_post_request(api_client, user):
    url = reverse('merchant-list')
    data = {
        "name": "Piper Cafe",
        "owner": user.id
    }
    api_client.force_authenticate(user=user)
    response = api_client.post(url, data, format='json')
    assert response.status_code == 201
    # assert response.json() == {
    #     'id': 2,
    #     'name': 'Piper Cafe',
    #     'owner': user.id
    # }


def test_merchant_detail_request(api_client, user, merchant):
    url = reverse('merchant-detail', args=(merchant.id,))
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == {
        'id': merchant.id,
        'name': 'Test merchant',
        'owner': user.id
    }


def test_merchant_put_request(api_client, user, merchant):
    url = reverse('merchant-detail', args=(merchant.id,))
    data = {
        "name": "Piper",
        "owner": user.id
    }
    api_client.force_authenticate(user=user)
    response = api_client.put(url, data, format='json')
    assert response.status_code == 200
    assert response.json() == {
        'id': merchant.id,
        'name': 'Piper',
        'owner': user.id
    }


def test_merchant_delete_request(api_client, user, merchant):
    url = reverse('merchant-detail', args=(merchant.id,))
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == 204
