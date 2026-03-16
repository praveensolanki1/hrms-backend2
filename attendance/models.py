from django.db import models
from employees.models import Employee


class Attendance(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent')
        ]
    )

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee} - {self.date} - {self.status}"