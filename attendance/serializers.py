from rest_framework import serializers
from .models import Attendance
from employees.models import Employee
from datetime import date


class AttendanceSerializer(serializers.ModelSerializer):

    employee = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all(),
        error_messages={
            "does_not_exist": "Employee does not exist",
            "incorrect_type": "Invalid employee ID"
        }
    )

    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, data):

        employee = data.get("employee")
        today = date.today()

        # Check duplicate attendance
        if Attendance.objects.filter(employee=employee, date=today).exists():
            raise serializers.ValidationError({
                "attendance": "Attendance already marked today"
            })

        return data