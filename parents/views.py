from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from parents.models import Parent
from parents.serializers import ParentSerializer


class ParentList(APIView):
    def get(self, request):
        school = request.user.school
        parents = Parent.objects.filter(school=school)
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        school = request.user.school
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            parent = serializer.save(school=school)
            parent_data = ParentSerializer(parent).data
            return Response({"the parent user has been created:": parent_data}, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class ParentDetail(APIView):

    def get(self, request, pk):
        school = request.user.school
        parent_obj = Parent.objects.get(id=pk)
        if parent_obj.school == school:
            serializer = ParentSerializer(parent_obj)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message" : "there is no such parent user in your school"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk):
        school = request.user.school
        parent_obj = Parent.objects.get(id=pk)
        if parent_obj.school == school:
            serializer = ParentSerializer(parent_obj, data=request.data)
            if serializer.is_valid():
                updated_parent = serializer.save()
                updated_parent_serializer = ParentSerializer(updated_parent)
                return Response(updated_parent_serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": "there is no such parent in your school"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        school = request.user.school
        parent_obj = Parent.objects.get(id=pk)
        if parent_obj.school == school:
            parent_obj.delete()
            return Response({"message" : f'the user {parent_obj.first_name} {parent_obj.last_name} was deleted'}, status = status.HTTP_204_NO_CONTENT)
        return Response({"message": "there is no such parent user in your school"}, status=status.HTTP_403_FORBIDDEN)




