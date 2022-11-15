from django.urls import path

from tools.views import AddressCsvUpload

urlpatterns = [
    path('address_csv_upload/', AddressCsvUpload.as_view(), name='adress_csv_upload'),
]