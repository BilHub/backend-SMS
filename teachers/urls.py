from django.urls import path

from teachers.views import TeacherList, TeacherDetail

urlpatterns = [
    path('', TeacherList.as_view(), name='teacher'),
    path('<int:pk>', TeacherDetail.as_view(), name='teacher_detail'),
]