from rest_framework import serializers
from nexong.models import Lesson, Student, LessonAttendance
from rest_framework.serializers import ModelSerializer
from datetime import datetime, timezone


class LessonSerializer(ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(
        many=True, required=True, queryset=Student.objects.all()
    )
    url = serializers.HyperlinkedIdentityField(view_name="lesson-detail")

    class Meta:
        model = Lesson
        fields = [
            "id",
            "name",
            "description",
            "capacity",
            "is_morning_lesson",
            "educator",
            "students",
            "start_date",
            "end_date",
            "url",
        ]

    def validate(self, attrs):
        validation_error = {}

        start_date = attrs.get("start_date")
        if start_date <= datetime.now(timezone.utc):
            validation_error["start_date"] = "The start date must be in the future."

        end_date = attrs.get("end_date")
        if end_date <= datetime.now(timezone.utc):
            validation_error["end_date"] = "The end date must be in the future."
        if end_date <= start_date:
            validation_error["end_date"] = "The end date must be after the start date."

        if validation_error:
            raise serializers.ValidationError(validation_error)

        return attrs


class LessonAttendanceSerializer(ModelSerializer):
    class Meta:
        model = LessonAttendance
        fields = [
            "id",
            "date",
            "lesson",
            "volunteer",
        ]

    def validate(self, attrs):
        validation_error = {}

        date = attrs.get("date")
        if date <= datetime.now(timezone.utc):
            validation_error["start_date"] = "The date must be now or in the past."
        if validation_error:
            raise serializers.ValidationError(validation_error)

        return attrs
