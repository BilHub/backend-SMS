from django.urls import path

from attendance.views import DailyAttendanceList, DailyAttendanceDetail

urlpatterns = [
    path('', DailyAttendanceList.as_view(), name='attendance'),
    path('<int:pk>/', DailyAttendanceDetail.as_view(), name='attendance_detail'),
]