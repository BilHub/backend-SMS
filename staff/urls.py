from django.urls import path

from staff.views import StaffList, StaffDetail

urlpatterns = [
    path('', StaffList.as_view(), name='staff'),
    path('<int:pk>', StaffDetail.as_view(), name='staff_detail'),
]