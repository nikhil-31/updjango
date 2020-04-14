import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from .test_model_fixtures import *

client = Client()


@pytest.fixture()
def function_fixture():
    return 3


@pytest.fixture(scope="module")
def module_fixture():
    return 1


def test_basic_test(function_fixture):
    assert function_fixture == 3

# @pytest.mark.parametrize(
#     'text_input, result', [('5+5', 10), ('1+4', 5), ('1+2', 3)]
# )
# def test_sum(text_input, result):
#     assert eval(text_input) == result
#
#
# @pytest.mark.django_db
# def test_user_create():
#     User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
#     assert User.objects.count() == 1
#
#
# @pytest.mark.django_db
# def test_unauthorized_request(api_client):
#     url = reverse('merchant-list')
#     response = api_client.get(url)
#     assert response.status_code == 401
