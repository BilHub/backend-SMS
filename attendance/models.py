from django.db import models

from course.models import Subject, Classroom, Level, Cycle
from students.models import Student
from teachers.models import Teacher


STATUS_CHOICES = [("present","PRESENT"), ("absent","ABSENT"), ("late","LATE")]


class DailyAttendence(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True, blank=True, related_name="subjects")
    cycle=models.ForeignKey(Cycle, on_delete=models.SET_NULL,null=True, blank=True)
    level=models.ForeignKey(Level, on_delete=models.SET_NULL,null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL,null=True, blank=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.date.strftime("%d/%m/%Y")) + "_" + str(self.subject)


class AttendanceItem(models.Model):
    attendance = models.ForeignKey(DailyAttendence, on_delete=models.CASCADE,
                                   related_name="attendance_items", null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="absent")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return str(self.date.strftime("%d/%m/%Y")) + "_" + str(self.student)
