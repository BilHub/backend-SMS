from django.urls import path, include

from authapp.views import LoginUser, SignUpUser, LogoutUser, UserDetail

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('signup/', SignUpUser.as_view(), name='signup'),
    path('user/<str:pk>/', UserDetail.as_view(), name='user_detail'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
]