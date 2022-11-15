import csv
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from tools.serializers import AddressCsvUploadSerializer


class AddressCsvUpload(APIView):
    def post(self, request, *args, **kwargs):
        # if request.user.is_superuser:
            serializer = AddressCsvUploadSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                csv_file = serializer['file_name']
                media_csv_file_name = csv_file.value
                csv_file_name = media_csv_file_name.replace("/media/csv/", "").replace("csv","json")
                csvFile = open(settings.BASE_DIR + media_csv_file_name, 'r')
                jsonFile = open(settings.BASE_DIR + f"/tools/fixtures/{csv_file_name}", 'w',
                                encoding='utf-8')
                reader = csv.DictReader(csvFile)
                for row in reader:
                    json.dump(row, jsonFile, ensure_ascii=False, indent=4, separators=(',', ': '))
                    jsonFile.write(',\n')
                return Response(serializer.data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response(status=status.HTTP_403_FORBIDDEN)
