from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, LevelViewSet, CycleViewSet

router = DefaultRouter()
router.register('subject', SubjectViewSet, basename='subject')
router.register('level', LevelViewSet, basename='level')
router.register('cycle', CycleViewSet, basename='cycle')

urlpatterns = router.urls
