from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from teachers.models import Teacher
from teachers.serializers import TeacherSerializer

class TeacherList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer