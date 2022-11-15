from django.urls import path

from parents.views import ParentList, ParentDetail

urlpatterns = [
    path('', ParentList.as_view(), name='parents'),
    path('<int:pk>/', ParentDetail.as_view(), name='parents_detail'),
]