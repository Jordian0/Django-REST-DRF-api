from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    #companies/{company_id}/employees
    @action(detail=True, methods=['GET'])
    def employees(self, request, pk=None):
        # print("Get employees of " + pk + " Company.")
        try:
            company = Company.objects.get(pk=pk)
            employees = Employee.objects.filter(company=company)
            employees_serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(employees_serializer.data)
        except Exception as e:
            print(e)
            return Response({'message':'Company might not exist!! Error'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# companies/{companyId}/employees
