from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import csrf_token_view
from .views import LoanRequestView
from .views import AdminLoginView
from .views import LoanRequestViewSet


router = DefaultRouter()
router.register(r'admin/loans', LoanRequestViewSet, basename='admin-loans')

urlpatterns = [
    path('loans', LoanRequestView.as_view(), name='loan-request'),
    path("csrf", csrf_token_view, name='csrf-token'),
    path('admin/login', AdminLoginView.as_view(), name='admin-login'),
    path('', include(router.urls)),
]