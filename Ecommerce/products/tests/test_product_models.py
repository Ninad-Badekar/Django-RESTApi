import pytest
from products.models import Product
from users.models import User

@pytest.mark.django_db
def test_product_creation():
    user = User.objects.create_user(
        email="seller@test.com",
        username="seller",
        password="test123"
    )

    product = Product.objects.create(
        name="Test Product",
        description="Test Description",
        price=100.0,
        quantity=5,
        seller=user
    )

    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 5
    assert product.seller == user