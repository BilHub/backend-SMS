from django.contrib import admin
from django.urls import path, include , re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from rest_framework import routers
# from course.urls import router as course_router

# router = routers.DefaultRouter()
# router.registry.extend(course_router.registry)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('authapp.urls')),
    path('api/v1/students/', include('students.urls')),
    path('api/v1/tools/', include('tools.urls')),
    path('api/v1/parents/', include('parents.urls')),
    path('api/v1/teachers/', include('teachers.urls')),
    path('api/v1/staff/', include('staff.urls')),
    path('api/v1/school/', include('school.urls')),
    path('api/v1/attendance/', include('attendance.urls')),
    path('api/v1/', include('course.urls')),
   #  path('api/v1', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
