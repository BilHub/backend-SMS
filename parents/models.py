from django.db import models

from authapp.models import CustomUser, School
from tools.models import Commune


class Parent(models.Model):
    GENDER_CHOICES = (('MALE', 'MALE'), ('FEMELLE', 'FEMELLE'))
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, null=True, blank=True, default="MALE")
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=250, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="parents")
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    has_account = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True, null=True, default="")
    commune = models.ForeignKey(Commune, blank=True, null=True, on_delete=models.SET_NULL)
    address = models.TextField(default="", max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name}_{self.last_name}'

    class Meta:
        ordering = ['last_name']
