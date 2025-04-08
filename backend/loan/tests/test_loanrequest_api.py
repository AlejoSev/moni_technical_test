import pytest
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
def test_loanrequest_api_success():
    """
    Checks the correct creation of an instance.
    """
    client = APIClient()
    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "M",
        "email": "alejoseverini@gmail.com",
        "amount": 1000000
    }

    response = client.post("/api/loans/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["msg"] in ["Loan rejected!", "Loan approved!"]


@pytest.mark.django_db
def test_loanrequest_api_missing_fields():
    """
    Checks that API returns 400 code when missing fields.
    """
    client = APIClient()
    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "M",
        "amount": 1000000
    }

    response = client.post("/api/loans/", data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in response.data


@pytest.mark.django_db
def test_loanrequest_api_negative_amount():
    """
    Checks that API returns 400 code when negative amount.
    """
    client = APIClient()
    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "M",
        "email": "alejoseverini@gmail.com",
        "amount": -1000000
    }

    response = client.post("/api/loans/", data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "amount" in response.data


@pytest.mark.django_db
def test_loanrequest_api_invalid_gender():
    """
    Checks that API returns 400 code when gender is invalid.
    """
    client = APIClient()
    data = {
        "dni": 40928594,
        "first_name": "Alejo",
        "last_name": "Severini Montanari",
        "gender": "X",
        "email": "alejoseverini@gmail.com",
        "amount": 1000000
    }

    response = client.post("/api/loans/", data, format="json")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "gender" in response.data
