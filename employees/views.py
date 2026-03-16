from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Q
from .models import Employee
from attendance.models import Attendance

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=False, url_path='summary')
    def summary(self, request):
        data = Employee.objects.annotate(
            total_present=Count('attendance__id', filter=Q(attendance__status='Present'))
        ).values('id', 'name', 'total_present')
        return Response(data)
