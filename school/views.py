from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from authapp.models import CustomUser
from school.models import School
from school.serializers import SchoolCreateSerializer, SchoolDetailSerializer


class SchoolList(APIView):

    def post(self, request, format=None):
        serializer = SchoolCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"school account created:", "data":serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # username = self.request.data["admins"][0]["username"]
            email = self.request.data["admins"][0]["email"]
            subdomain = self.request.data["subdomain"]
            if School.objects.filter(subdomain=subdomain):
                return Response({
                    "message": "subdomain already exists"
                }, status=status.HTTP_400_BAD_REQUEST)
            elif CustomUser.objects.filter(email=email):
                return Response({
                    "message":"User already exists"
                }, status=status.HTTP_400_BAD_REQUEST)
            # elif CustomUser.objects.filter(username=username):
            #     return Response({
            #         "message":"username already exists"
            #     }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SchoolDetail(APIView):

    def get(self, request,pk):
        school_obj = School.objects.get(id=pk)
        serializer = SchoolDetailSerializer(school_obj)
        return Response(
            serializer.data
            , status=status.HTTP_200_OK
        )

    def put(self, request, pk):
        school_obj = School.objects.get(id=pk)
        serializer = SchoolDetailSerializer(school_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":f'school {serializer.data["school_name"]} was updated'}
                , status = status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,pk):
        school_obj = School.objects.get(id=pk)
        school_obj.delete()
        return Response({"message":f'school {school_obj.school_name} was deleted !'})


        

