import requests
import json
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import LoanRequest
from .serializers import LoanRequestSerializer
from .const import STATUS_APPROVED
from .const import STATUS_REJECTED
from .const import LoanRequestStatus


class LoanRequestView(APIView):
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
