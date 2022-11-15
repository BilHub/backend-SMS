from rest_framework import serializers

from tools.models import CsvUpload


class AddressCsvUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = CsvUpload
        fields = ('file_name',)