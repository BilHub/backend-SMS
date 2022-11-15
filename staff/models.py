import datetime

from django.db import models

from authapp.models import CustomUser, School
from tools.models import Commune

class Staff(models.Model):
    GENDER_CHOICES = (('MALE', 'MALE'), ('FEMELLE', 'FEMELLE'))
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True, default="MALE")
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name="admin_user")
    school=models.OneToOneField(School,on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100, default="")
    first_name = models.CharField(max_length=100, default="")
    # photo = models.ImageField(upload_to='students',
    #                           default='studentavar.png')
    date_of_birth = models.DateField(blank=True, null=True)
    registration_number = models.CharField(max_length=6, unique=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(default="",max_length=255, unique=True, null=False, blank=False)
    commune = models.ForeignKey(Commune,unique=False, null=True ,on_delete=models.SET_NULL)
    address = models.TextField(default="", max_length=255, unique=False, blank=True, null=True)
    # created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.first_name

    # groupe sanguin
    # class Meta:
    #     ordering = ['last_name']
