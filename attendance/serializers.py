from rest_framework import serializers
from datetime import datetime

from attendance.models import DailyAttendence, AttendanceItem


class AttendanceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceItem
        fields = ('id', 'student', 'status')


class DailyAttendanceSerializer(serializers.ModelSerializer):
    attendance_items = AttendanceItemSerializer(many=True)
    class Meta:
        model = DailyAttendence
        fields = ('subject','cycle', 'level', 'teacher','date', 'classroom', 'attendance_items')

    def create(self, validated_data):
        items_data = validated_data.pop("attendance_items")
        daily_attendance = DailyAttendence.objects.create(**validated_data)
        for item in items_data:
            AttendanceItem.objects.create(**item, attendance=daily_attendance)
        return daily_attendance

    def update(self, instance, validated_data):

        items_data = validated_data.pop("attendance_items")
        attendance_items = instance.attendance_items
        instance.module = validated_data.get("module", instance.module)
        instance.teacher = validated_data.get("teacher", instance.teacher)
        instance.date = validated_data.get("date", instance.date)
        instance.classroom = validated_data.get("classroom", instance.classroom)
        instance.save()

        for item_data in items_data:
            item = AttendanceItem.objects.get(student=item_data['student'])
            item.student = item_data.get("student", item.student)
            item.status = item_data.get("status", item.status)
            item.save()

        return instance
    
    def to_representation(self, data):
        data = super(DailyAttendanceSerializer, self).to_representation(data)
        data["date"] = data["date"].date().strftime("%d/%m/%Y")
        return data
