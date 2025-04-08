from django.db import models

class LoanRequest(models.Model):
	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]

	dni = models.PositiveIntegerField()
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	email = models.EmailField()
	amount = models.PositiveIntegerField()
	approved = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name} ({self.dni})"