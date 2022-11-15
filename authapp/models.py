import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, Group

from school.models import School
from tools.models import Commune

class UserType(models.Model):
    type = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.type

class UserGroup(models.Model):
    user_group = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.user_group

class CustomUser(AbstractUser):
    GENDER_CHOICES = (('male','MALE'), ('female','FEMALE'))
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True, default="male")
    # username = models.CharField(default="", max_length=250, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=250, default="")
    last_name = models.CharField(max_length=250, default="")
    user_group=models.ForeignKey(UserGroup,on_delete=models.SET_NULL, null=True, blank=True, to_field="user_group")
    school=models.ForeignKey(School,on_delete=models.CASCADE, related_name="admins", null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, blank=True, null=True, default="")
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(max_length=250, null=True, blank=True, default="")
    date_of_birth = models.DateField(blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    subdomain = models.CharField(max_length=200, null=True, blank=True)
    # photo = models.ImageField(upload_to='students', default='studentavar.png')

    def __str__(self):
        return self.email






