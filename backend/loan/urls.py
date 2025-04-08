from django.urls import path
from .views import LoanRequestView

urlpatterns = [
    path('loans/', LoanRequestView.as_view(), name='loan-request'),
]