from django.urls import path

from school.views import SchoolList, SchoolDetail

urlpatterns = [
        path('create_school_account/', SchoolList.as_view(), name='school_account'),
        path('<str:pk>/', SchoolDetail.as_view(), name='school_detail'),
]