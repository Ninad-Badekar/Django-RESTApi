import pytest

@pytest.mark.django_db
def test_create_product(auth_client):
    payload = {
        "name": "iPhone 15",
        "price": 120000,
        "quantity": 5
    }

    response = auth_client.post("/api/products/", payload)

    assert response.status_code == 201
    assert response.data["name"] == "iPhone 15"


@pytest.mark.django_db
def test_get_products(api_client, product):
    response = api_client.get("/api/products/")

    assert response.status_code == 200
    assert len(response.data) > 0
