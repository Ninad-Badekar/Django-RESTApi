import pytest
from cart.models import Cart

@pytest.mark.django_db
def test_cart_model(user, product):
    cart = Cart.objects.create(
        user=user,
        product=product,
        quantity=3
    )

    assert cart.user == user
    assert cart.product == product
    assert cart.quantity == 3
