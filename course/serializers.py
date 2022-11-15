from rest_framework import serializers

from course.models import Cycle, Level, Subject


class SubjectSerializer(serializers.ModelSerializer):
    students_number = serializers.CharField(required=False)
    teachers_list = serializers.ListField(required=False)
    class Meta:
        model = Subject
        fields = ('id','subject_name', 'level','cycle','students_number', 'teachers_list')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = '__all__'


