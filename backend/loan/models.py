from django.db import models

class LoanRequest(models.Model):
	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]

	dni = models.CharField(max_length=16)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	email = models.EmailField()
	amount = models.DecimalField(max_digits=10, decimal_places=0)
	approved = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.dni})"