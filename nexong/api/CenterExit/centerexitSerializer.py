from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from nexong.models import CenterExitAuthorization, LessonEvent, Student


class CenterExitSerializer(ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        many=False, required=True, queryset=Student.objects.all()
    )
    lesson_event = serializers.PrimaryKeyRelatedField(
        many=False, required=True, queryset=LessonEvent.objects.all()
    )

    class Meta:
        model = CenterExitAuthorization
        fields = [
            "id",
            "authorization",
            "student",
            "is_authorized",
            "lesson_event",
        ]
