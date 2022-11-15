from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from authapp.models import CustomUser
from authapp.serializers import SignUpUserSerializer, LogoutUserSerializer, CustomTokenObtainSerializer

#  convert into generic view
class SignUpUser(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        user_data = request.data
        serializer = SignUpUserSerializer(data=user_data)
        if serializer.is_valid():

            school = request.user.school
            if school:
                user = serializer.save(school=school)
                user_group = serializer.data["user_group"]
                group_name, created = Group.objects.get_or_create(name=user_group)
                group_name.user_set.add(user)
                user_serializer = SignUpUserSerializer(user)
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            return Response({"erreur":"the creator must have a school_id"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  convert into generic view
class UserDetail(APIView):

    def get(self, request, pk):
        user_obj = CustomUser.objects.get(id=pk)
        serializer = SignUpUserSerializer(user_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        user_obj = CustomUser.objects.get(id=pk)
        serializer = SignUpUserSerializer(user_obj, data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_serializer = SignUpUserSerializer(user)
            return Response({"message": f'the user {serializer.data["username"]} was updated', "data":user_serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_obj = CustomUser.objects.get(id=pk)
        user_obj.delete()
        # user_obj.is_active=False
        # user_obj.save()
        return Response({"message": f'the user {user_obj.username} was deleted !'}, status=status.HTTP_200_OK)


class LogoutUser(APIView):
    def post(self, request, format=None):
        serializer = LogoutUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("succesfull logout", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUser(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


