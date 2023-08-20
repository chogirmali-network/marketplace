from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .serializers import AddCompanySerializer, AddEmployeeSerializer
from .models import Company, Employee


class AddCompanyView(APIView):
    def post(self, request):
        serializer = AddCompanySerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class AddEmployeeView(APIView):
    def post(self, request):
        serializer = AddEmployeeSerializer(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
