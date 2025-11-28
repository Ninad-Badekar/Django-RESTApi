import pytest
from cart.models import Cart

@pytest.mark.django_db
def test_add_to_cart(auth_client, product):
    payload = {
        "product": product.id,
        "quantity": 2
    }

    response = auth_client.post("/api/cart/", payload)

    assert response.status_code == 201
    assert response.data["quantity"] == 2


@pytest.mark.django_db
def test_cart_list(auth_client, product):
    Cart.objects.create(user=auth_client.handler._force_user, product=product, quantity=1)

    response = auth_client.get("/api/cart/")

    assert response.status_code == 200
    assert len(response.data) == 1
