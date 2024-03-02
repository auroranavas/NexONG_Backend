from rest_framework import serializers
from nexong.models import Lesson, Student, LessonAttendance, LessonEvent, Educator, Volunteer
from rest_framework.serializers import ModelSerializer


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
            "url",
        ]

class LessonAttendanceSerializer(ModelSerializer):

    class Meta:
        model = LessonAttendance
        fields = [
            "id",
            "date",
            "lesson",
            "volunteer",
        ]

class LessonEventSerializer(ModelSerializer):
    educators = serializers.PrimaryKeyRelatedField(
        many=True, required=True, queryset=Educator.objects.all()
    )
    attendees = serializers.PrimaryKeyRelatedField(
        many=True, required=True, queryset=Student.objects.all()
    )
    volunteers = serializers.PrimaryKeyRelatedField(
        many=True, required=False, queryset=Volunteer.objects.all()
    )


    class Meta:
        model = LessonEvent
        fields = [
            "id",
            "name",
            "description",
            "place",
            "max_volunteers",
            "start_date",
            "end_date",
            "lesson",
            "price",
            "educators",
            "attendees",
            "volunteers",
        ]