from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from products.views import product_detail
from mixer.backend.django import mixer
from django.test import TestCase
import pytest

# @pytest.mark.django_db
# class TestViews(TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         super(TestViews, cls).setUpClass()
#         mixer.blend('products.Product')
#         cls.factory = RequestFactory()
#
#     def test_product_detail_authenticated(self):
#         path = reverse('detail', kwargs={
#             'pk': 1
#         })
#         request = self.factory.get(path)
#         request.user = mixer.blend(User)
#
#         response = product_detail(request, pk=1)
#         assert response.status_code == 200
#
#     def test_product_detail_unuthenticated(self):
#         path = reverse('detail', kwargs={
#             'pk': 1
#         })
#         request = self.factory.get(path)
#         request.user = AnonymousUser()
#
#         response = product_detail(request, pk=1)
#         assert response.status_code == 302
#         assert 'accounts/login' in response.url

@pytest.fixture(scope='module')
def factory():
    return RequestFactory()

@pytest.fixture
def product(db):
    return mixer.blend('products.Product')

def test_product_detail_authenticated(factory, product):
    path = reverse('detail', kwargs={
        'pk': 1
    })
    request = factory.get(path)
    request.user = mixer.blend(User)

    response = product_detail(request, pk=1)
    assert response.status_code == 200


def test_product_detail_unuthenticated(factory, product):
    path = reverse('detail', kwargs={
        'pk': 1
    })
    request = factory.get(path)
    request.user = AnonymousUser()

    response = product_detail(request, pk=1)
    assert response.status_code == 302
    assert 'accounts/login' in response.url