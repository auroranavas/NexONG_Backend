from rest_framework import serializers
from nexong.models import Event, User
from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    # attendees is optional at creation
    attendees = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False
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
            "educators",
        ]

    def validate_educators(self, value):
        if not value:
            raise serializers.ValidationError("Must provide at least 1 educator.")
        return value
