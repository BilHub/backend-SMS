from django.db import models

from tools.models import Commune

class School(models.Model):
    school_name = models.CharField(max_length=100, default="school", null=False, blank=False)
    subdomain = models.CharField(max_length=100,unique=True)
    commune = models.ForeignKey(Commune, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.school_name