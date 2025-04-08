import pytest
from loan.models import LoanRequest
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import timedelta

@pytest.mark.django_db
def test_loanrequest_creation():
	"""
	Check the correct creation of the instance, based on the id and the time of creation.
	"""
	loan = LoanRequest.objects.create(
		dni=40928594,
		first_name='Alejo',
		last_name='Severini Montanari',
		gender='M',
		email='alejoseverini@gmail.com',
		amount=1000000,
		approved=True)

	assert loan.id is not None
	assert abs(loan.created_at - timezone.now()) < timedelta(seconds=1)


@pytest.mark.django_db
def test_loanrequest_str():
	"""
	Check if the __str__ function of the model returns the expected value.
	"""
	loan = LoanRequest.objects.create(
		dni=40928594,
		first_name='Alejo',
		last_name='Severini Montanari',
		gender='M',
		email='alejoseverini@gmail.com',
		amount=1000000,
		approved=True)

	expected_str = "Alejo Severini Montanari (40928594)"
	assert str(loan) == expected_str


@pytest.mark.django_db
def test_loanrequest_invalid_email():
	"""
	Check if instance creation raises ValidationError when email is an invalid string.
	"""
	loan = LoanRequest.objects.create(
		dni=40928594,
		first_name='Alejo',
		last_name='Severini Montanari',
		gender='M',
		email='this_is_an_invalid_email',
		amount=1000000,
		approved=True)

	with pytest.raises(ValidationError):
		loan.full_clean() 


@pytest.mark.django_db
def test_loanrequest_invalid_gender():
	"""
	Check if instance creation raises ValidationError when gender is not one
	of the available choices.
	"""
	loan = LoanRequest.objects.create(
		dni=40928594,
		first_name='Alejo',
		last_name='Severini Montanari',
		gender='X',
		email='alejoseverini@gmail.com',
		amount=1000000,
		approved=True)

	with pytest.raises(ValidationError):
		loan.full_clean()


@pytest.mark.django_db
def test_loanrequest_negative_amount():
	"""
	Check if instance creation raises ValidationError when amount is negative.
	"""
	loan = LoanRequest(
		dni=40928594,
		first_name='Alejo',
		last_name='Severini Montanari',
		gender='M',
		email='alejoseverini@gmail.com',
		amount=-1000000,
		approved=True)

	with pytest.raises(ValidationError):
		loan.full_clean()


@pytest.mark.django_db
def test_loanrequest_negative_dni():
	"""
	Check if instance creation raises ValidationError when dni is negative.
	"""
	loan = LoanRequest(
		dni=-40928594,
		first_name='Alejo',
		last_name='Severini Montanari',
		gender='M',
		email='alejoseverini@gmail.com',
		amount=1000000,
		approved=True)

	with pytest.raises(ValidationError):
		loan.full_clean()
