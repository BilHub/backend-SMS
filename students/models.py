import datetime

from django.db import models

from authapp.models import CustomUser, School
from tools.models import Commune
from course.models import Subject

class Student_group(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student(models.Model):
    BLOOD_GROUP_CHOICES = (
        ('A_POSITIVE', 'A_POSITIVE'),
        ('O_POSITIVE', 'O_POSITIVE'),
        ('b_POSITIVE', 'B_POSITIVE'),
        ('ab_POSITIVE', 'AB_POSITIVE'),
        ('A_NEGATIVE', 'A_NEGATIVE'),
        ('O_NEGATIVE', 'O_NEGATIVE'),
        ('B_NEGATIVE', 'B_NEGATIVE'),
        ('AB_NEGATIVE', 'AB_NEGATIVE')
    )
    GENDER_CHOICES = (('MALE','MALE'), ('FEMALE','FEMALE'))
    user=models.OneToOneField(CustomUser,on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE, related_name="student_school")
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    has_account = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True, null=True, default="")
    # change the address to city, state, zip
    # commune = models.ForeignKey(Commune, blank=True, null=True, on_delete=models.SET_NULL)
    address = models.TextField(default="", max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True, default="MALE")
    blood_group = models.CharField(max_length=50, choices=BLOOD_GROUP_CHOICES, null=True, blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    subjects = models.ManyToManyField(Subject,blank=True, null=True, related_name="students")

    class Meta:
        ordering=['last_name']

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'






