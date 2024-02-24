from rest_framework import serializers
from nexong.models import Event, User
from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.filter(educator__isnull=False)
    )

    class Meta:
        model = Event
        fields = [
            "name",
            "description",
            "place",
            "capacity",
            "max_volunteers",
            "start_date",
            "end_date",
            "lesson",
            "attendees",
        ]

    def get_attendees(self, obj):
        attendees = User.objects.filter(educator__isnull=False)
        return attendees

    def validate_educators(self, value):
        if not value:
            raise serializers.ValidationError("Must provide at least 1 educator.")
        return value
