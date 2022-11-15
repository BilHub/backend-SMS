from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from authapp.models import CustomUser
from authapp.serializers import SignUpAdminSerializer
from school.models import School

class SchoolCreateSerializer(serializers.ModelSerializer):
    admins = SignUpAdminSerializer(many=True)

    class Meta:
        model = School
        # fields = ["id","school_name","subdomain", "commune", "address", "admins"]
        fields = '__all__'

    def create(self, validated_data):
        admins_data = validated_data.pop("admins")
        school_obj = School.objects.create(**validated_data)
        for admin in admins_data:
            password=make_password(admin["password"])
            email=admin["email"]
            first_name=admin["first_name"]
            last_name=admin["last_name"]
            subdomain = validated_data["subdomain"]
            user = CustomUser.objects.create(password=password, email=email, is_staff=True, first_name=first_name, last_name=last_name, subdomain=subdomain)
            user.save()
        return school_obj

class SchoolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        # fields = ["id","school_name","subdomain", "commune", "address"]
        fields = '__all__'