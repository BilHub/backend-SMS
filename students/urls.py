from django.urls import path

from students.views import StudentList, StudentDetail

urlpatterns = [
    path('', StudentList.as_view(), name='students'),
    path('<int:pk>/', StudentDetail.as_view(), name='student_detail'),
]