import pytest
from pytest_factoryboy import register
from .factory import CategoryFactory, BrandFactory, ProductFactory

from rest_framework.test import APIClient

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)


@pytest.fixture
def api_client():
    return APIClient
