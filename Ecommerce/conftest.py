import pytest
from rest_framework.test import APIClient
from users.models import User
from products.models import Product

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", email="test@example.com", password="password123")

@pytest.fixture
def auth_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.fixture
def product(db, user):
    return Product.objects.create(
        name="Test Product",
        description="A product for testing",
        price=100,
        quantity=10,
        seller=user
    )
