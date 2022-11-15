from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import json 

from .models import CustomUser
# from school.serializers import SchoolDetailSerializer 

class SignUpAdminSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = '__all__'


class SignUpUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        # fields = ["id","username", "password", "email", "is_staff","is_superuser", "user_type", "first_name", "last_name", "date_of_birth", "commune", "address", "school", "user_group"]
        fields = '__all__'
        read_only_fields=("school",)


class LogoutUserSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    default_error_messages = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data =  super().validate(attrs)
        # data["school"] = self.user.school
        data["user"] = SignUpUserSerializer(self.user).data
        data["school_subdomain"] = self.user.school.subdomain
        return data
