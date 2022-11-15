from django.contrib import admin
from .models import CustomUser, UserGroup, UserType

admin.site.register(CustomUser)
admin.site.register(UserGroup)
admin.site.register(UserType)