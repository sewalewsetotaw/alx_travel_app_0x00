# listings/views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class SampleAPIView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to ALX Travel App"})
