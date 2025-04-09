import requests
import json
import os

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import LoanRequest
from .serializers import LoanRequestSerializer
from .const import STATUS_APPROVED
from .const import STATUS_REJECTED
from .const import LoanRequestStatus


@ensure_csrf_cookie
def csrf_token_view(request):
    return JsonResponse({'msg': 'CSRF cookie set'})


@method_decorator(csrf_exempt, name='dispatch')
class LoanRequestView(APIView):
	http_method_names = ['post']
	authentication_classes = []
	permission_classes = []

	def post(self, request: Request) -> Response:
		"""
		Endpoint that creates the LoanRequest object.
		"""
		serializer = LoanRequestSerializer(data=request.data)

		if serializer.is_valid():
			dni = serializer.validated_data['dni']
			loan_request_status = self.check_external_api(dni)

			approved = True if loan_request_status == STATUS_APPROVED else False

			loan = LoanRequest.objects.create(
				approved=approved,
				**serializer.validated_data
			)

			return Response({
				'msg': f'Loan {loan_request_status}!'
			}, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def check_external_api(self, dni: int) -> LoanRequestStatus:
		"""
		Makes the POST request to the external API, using the requested DNI to check if the
		loan is approved or rejected for that user.
		"""
		url = os.getenv("EXTERNAL_API_URL")

		headers = {
			'Content-Type': 'application/json',
			'x-api-key': os.getenv("EXTERNAL_API_KEY")
			}

		payload = json.dumps({
			"cuil": dni
			})
		
		try:
			response = requests.request("POST", url, headers=headers, data=payload)

			data = response.json()

			return data.get('status', STATUS_REJECTED)
		
		except Exception as e:
			print("Error callign external API:", e)

			return STATUS_REJECTED


class AdminLoginView(APIView):
	authentication_classes = []
	permission_classes = []

	def post(self, request):
		username = request.data.get('username')
		password = request.data.get('password')

		print(f'Creds: {username}:{password}')

		user = authenticate(username=username, password=password)

		if user and user.is_staff:
			login(request, user)
			return Response({'success': True, 'msg': 'Login exitoso'}, status=status.HTTP_200_OK)
		else:
			return Response({'success': False, 'msg': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


class LoanRequestViewSet(ModelViewSet):
	queryset = LoanRequest.objects.all()
	serializer_class = LoanRequestSerializer
	permission_classes = [AllowAny]
