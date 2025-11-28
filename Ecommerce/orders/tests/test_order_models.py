import pytest
from orders.models import Order
from products.models import Product
from users.models import User

@pytest.mark.django_db
def test_order_creation():
    user = User.objects.create_user(
        email="buyer@test.com",
        username="buyer",
        password="test123"
    )

    product = Product.objects.create(
        name="Phone",
        description="Smartphone",
        price=999,
        quantity=10,
        seller=user
    )

    order = Order.objects.create(
        user=user,
        product=product,
        quantity=2
    )

    assert order.user == user
    assert order.product == product
    assert order.quantity == 2
    assert order.ordered_at is not None
