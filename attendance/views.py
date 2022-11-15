from rest_framework.views import APIView, status
from rest_framework.response import Response

from attendance.models import DailyAttendence
from attendance.serializers import DailyAttendanceSerializer

class DailyAttendanceList(APIView):

    def get(self, request):
        attendance_list = DailyAttendence.objects.all()
        serializer = DailyAttendanceSerializer(attendance_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DailyAttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "attendance created successfully"}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class DailyAttendanceDetail(APIView):
    def get(self, request, pk):
        print('here')
        attendance_obj = DailyAttendence.objects.get(id=pk)
        serializer = DailyAttendanceSerializer(attendance_obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        attendance_obj = DailyAttendence.objects.get(id=pk)
        serializer = DailyAttendanceSerializer(attendance_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": f'the attendance {attendance_obj.module} {attendance_obj.date} was updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attendance_obj = DailyAttendence.objects.get(id=pk)
        attendance_obj.delete()
        return Response({"message": f'the attendance {attendance_obj.module} {attendance_obj.date} was deleted !'},
                        status=status.HTTP_204_NO_CONTENT)