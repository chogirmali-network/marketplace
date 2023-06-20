from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee


class CompanyView(APIView):
    def get(self, request, company_id=None):
        if company_id:
            company = get_object_or_404(Company, id=company_id)
            serializer = CompanySerializer(instance=company)
        else:
            companys = Company.objects.all()
            serializer = CompanySerializer(instance=companys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, company_id):
        company = get_object_or_404(Company, pk=company_id)
        data = request.data
        serializer = CompanySerializer(instance=company, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self, request, company_id):
        Company.objects.filter(id=company_id).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class EmployeeView(APIView):
    def get(self, request, employee_id=None):
        if employee_id:
            employee = get_object_or_404(Employee, id=employee_id)
            serializer = EmployeeSerializer(instance=employee)
        else:
            employee = Employee.objects.all()
            serializer = EmployeeSerializer(instance=employee, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)

    def put(self, request, employee_id):
        isinstance = get_object_or_404(Employee, id=employee_id)
        serializer = EmployeeSerializer(instance=isinstance, data=request.data, partial=True)
        serializer.save()
        return Response({}, status=status.HTTP_200_OK)

    def delete(self, request, employee_id):
        Employee.objects.filter(id=employee_id).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)
