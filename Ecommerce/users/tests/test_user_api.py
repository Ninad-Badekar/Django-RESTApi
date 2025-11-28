import pytest

@pytest.mark.django_db
def test_user_registration(api_client):
    payload = {
        "email": "newuser@example.com",
        "password": "Strongpass123"
    }

    response = api_client.post("/api/users/register/", payload)

    assert response.status_code == 201
    assert response.data["email"] == payload["email"]
