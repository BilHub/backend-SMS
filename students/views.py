from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import Group


from authapp.serializers import SignUpUserSerializer
from students.models import Student
from students.serializers import StudentSerializer

class StudentList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        school = user.school
        students = Student.objects.filter(school=school)
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user_data = request.data
        school = request.user.school

        if school:
            if 'username' in request.data.keys() and 'password' in request.data.keys():
                serializer = SignUpUserSerializer(data=user_data)
            else:
                serializer = StudentSerializer(data=request.data)

            if serializer.is_valid():
                user_obj = serializer.save(school=school)
                if 'username' in request.data.keys():
                    user_group = serializer.data["user_group"]
                    group_name, created = Group.objects.get_or_create(name=user_group)
                    group_name.user_set.add(user_obj)
                    user_serializer = SignUpUserSerializer(user_obj)
                else:
                    user_serializer = StudentSerializer(user_obj)
                return Response(user_serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"erreur": "the creator must have a school_id"}, status=status.HTTP_403_FORBIDDEN)


class StudentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        school = request.user.school
        student_obj = Student.objects.get(id=pk)
        if student_obj.school == school:
            serializer = StudentSerializer(student_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "there is no such student in your school"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        school = request.user.school
        if school:
            student_obj = Student.objects.get(id=pk)
            if student_obj.school == school:
                data_student = request.data
                data_student["school"] = school.id
                serializer = StudentSerializer(student_obj, data=data_student)
                if serializer.is_valid():
                    student = serializer.save()
                    student_serializer = StudentSerializer(student)
                    return Response(student_serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"message": "there is no such student in your school"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"erreur" : "the creator must have a school_id"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        school = request.user.school
        if school:
            student_obj = Student.objects.get(id=pk)
            if student_obj.school == school:
                student_obj.delete()
                return Response({"message": f'the student {student_obj.username} was deleted !'}, status=status.HTTP_200_OK)
            return Response({"message": "there is no such student in your school"}, status=status.HTTP_403_FORBIDDEN)
        return Response({"erreur": "the creator must have a school_id"}, status=status.HTTP_400_BAD_REQUEST)
