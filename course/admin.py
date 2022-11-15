from django.contrib import admin

from course.models import Classroom, Subject, Level, Cycle

admin.site.register(Cycle)
admin.site.register(Level)
admin.site.register(Subject)
admin.site.register(Classroom)
