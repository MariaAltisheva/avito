import pytest


@pytest.mark.django_db
def test_ad_create(client, user, category, access_token):
    data = {
        "author": user.pk,
        "category": category.pk,
        "name": "Test Ad Name",
        "price": 432,
        "description": "",
        "is_published": False
    }

    expected_data = {
        "id": 1,
        "is_published": False,
        "name": "Test Ad Name",
        "price": 432,
        "description": "",
        "image": None,
        "author": 2,
        "category": 2
    }
    response = client.post('/ad/', data, content_type="application/json")
    assert response.status_code == 201
    assert response.data == expected_data
