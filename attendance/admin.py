from django.contrib import admin

from attendance.models import DailyAttendence, AttendanceItem

admin.site.register(DailyAttendence)
admin.site.register(AttendanceItem)