from django.db import models

class Wilaya(models.Model):
    name = models.CharField(default="", max_length=200, unique=True, null=True, blank=True)
    def __str__(self):
        return self.name

class Commune(models.Model):
    name = models.CharField(default="", max_length=200, unique=False, null=True, blank=True)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class CsvUpload(models.Model):
    file_name = models.FileField(blank=False, null=False, upload_to='csv')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file_name