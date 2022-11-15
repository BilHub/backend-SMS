import datetime

from django.db import models

from authapp.models import CustomUser, School
from course.models import Subject
from tools.models import Commune

class Teacher(models.Model):
    GENDER_CHOICES = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'))
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True, default="MALE")
    user=models.OneToOneField(CustomUser,on_delete=models.SET_NULL, null=True, blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE, related_name="teacher_school", null=True)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(blank=True, null=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    has_account = models.BooleanField(default=False)
    phone = models.CharField(max_length=11, blank=True, null=True)
    commune = models.ForeignKey(Commune, blank=True, null=True, on_delete=models.SET_NULL)
    address = models.TextField(default="", max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    subject = models.ManyToManyField(Subject, null=True, blank=True, related_name='teachers')
    # photo = models.ImageField(upload_to='students',
    #                           default='teacheravatar.png')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'

    # groupe sanguin
    class Meta:
        ordering = ['last_name']