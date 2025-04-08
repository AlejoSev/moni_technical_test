import requests
import json
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import LoanRequest
from .serializers import LoanRequestSerializer
from .const import STATUS_APPROVED
from .const import STATUS_REJECTED


class LoanRequestView(APIView):
	def post(self, request):
		serializer = LoanRequestSerializer(data=request.data)

		if serializer.is_valid():
			dni = serializer.validated_data['dni']
			approved = self.check_external_api(dni)

			loan = LoanRequest.objects.create(
				approved=approved,
				**serializer.validated_data
			)

			return Response({
				'msg': f'Loan {approved}!'
			}, status=status.HTTP_201_CREATED)
		
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def check_external_api(self, dni):
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
