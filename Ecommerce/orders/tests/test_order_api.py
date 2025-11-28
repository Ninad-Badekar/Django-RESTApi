import pytest

@pytest.mark.django_db
def test_create_order(auth_client, product):
    payload = {
        "product": product.id,
        "quantity": 1
    }

    response = auth_client.post("/api/orders/", payload)

    assert response.status_code == 201
    assert response.data["quantity"] == 1


@pytest.mark.django_db
def test_get_orders(auth_client, product):
    auth_client.post("/api/orders/", {
        "product": product.id,
        "quantity": 2
    })

    response = auth_client.get("/api/orders/")

    assert response.status_code == 200
    assert len(response.data) > 0
