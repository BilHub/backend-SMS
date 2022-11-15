from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        # fields = ["id","email", "first_name", "last_name", "username", "password", "school"]
        fields = '__all__'
        read_only_fields = ('school',)


