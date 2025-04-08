from django.db import models

class LoanRequest(models.Model):
	GENDER_CHOICES = [
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]

	dni = models.PositiveIntegerField(blank=False, null=False)
	first_name = models.CharField(max_length=64, blank=False, null=False)
	last_name = models.CharField(max_length=64, blank=False, null=False)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False)
	email = models.EmailField(blank=False, null=False)
	amount = models.PositiveIntegerField(blank=False, null=False)
	approved = models.BooleanField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name} ({self.dni})"