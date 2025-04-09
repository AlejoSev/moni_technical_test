import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def get_access_token():
    """
    Access token used in tests.
    """
    user = User.objects.create_user(username='testuser', password='password123')

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    return access_token


@pytest.mark.django_db
def test_loanrequest_api_success(get_access_token):
    """
    Checks the correct creation of an instance.
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_access_token}')

    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "M",
        "email": "alejoseverini@gmail.com",
        "amount": 1000000
    }

    response = client.post("/api/loans", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["msg"] in ["Loan rejected!", "Loan approved!"]


@pytest.mark.django_db
def test_loanrequest_api_missing_fields(get_access_token):
    """
    Checks that API returns 400 code when missing fields.
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_access_token}')

    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "M",
        "amount": 1000000
    }

    response = client.post("/api/loans", data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data


@pytest.mark.django_db
def test_loanrequest_api_negative_amount(get_access_token):
    """
    Checks that API returns 400 code when negative amount.
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_access_token}')

    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "M",
        "email": "alejoseverini@gmail.com",
        "amount": -1000000
    }

    response = client.post("/api/loans", data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "amount" in response.data


@pytest.mark.django_db
def test_loanrequest_api_invalid_gender(get_access_token):
    """
    Checks that API returns 400 code when gender is invalid.
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {get_access_token}')

    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "X",
        "email": "alejoseverini@gmail.com",
        "amount": 1000000
    }

    response = client.post("/api/loans", data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "gender" in response.data
