from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from staff.models import Staff
from staff.serializers import StaffSerializer

class StaffList(ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffDetail(RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer