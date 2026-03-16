from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Attendance
from .serializers import AttendanceSerializer
from django.db.models import Count, Q

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=False, methods=['get'], url_path='summary')
    def summary(self, request):
        summary_data = Attendance.objects.values(
            'employee__id', 'employee__name'
        ).annotate(
            total_present=Count('id', filter=Q(status='Present'))
        )
        return Response(summary_data)

    @action(detail=False, methods=['get'], url_path='employee/(?P<employee_id>[^/.]+)')
    def employee_attendance(self, request, employee_id=None):
        records = Attendance.objects.filter(employee_id=employee_id)
        serializer = AttendanceSerializer(records, many=True)
        return Response(serializer.data)