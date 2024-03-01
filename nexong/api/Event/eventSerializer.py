from rest_framework import serializers
from nexong.models import Event, User
from rest_framework.serializers import ModelSerializer
from datetime import datetime, timezone


class EventSerializer(ModelSerializer):
    # attendees is optional at creation
    attendees = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True, required=False
    )
    url = serializers.HyperlinkedIdentityField(view_name="event-detail")

    class Meta:
        model = Event
        fields = [
            "id",
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
            "url",
        ]

    def validate_educators(self, value):
        if not value:
            raise serializers.ValidationError("Must provide at least 1 educator.")
        return value

    def validate(self, attrs):
        validation_error = {}

        attendees_emails = attrs.get("attendees")
        attendees_qs = User.objects.filter(email__in=attendees_emails)

        num_attendees = attendees_qs.all().count()
        max_capacity = attrs.get("capacity")
        if max_capacity < num_attendees:
            validation_error[
                "capacity"
            ] = "The max capacity must be higher or equal to the number of attendees selected."

        start_date = attrs.get("start_date")
        if start_date <= datetime.now(timezone.utc):
            validation_error["start_date"] = "The start date must be in the future."

        end_date = attrs.get("end_date")
        if end_date <= datetime.now(timezone.utc):
            validation_error["end_date"] = "The end date must be in the future."
        if end_date <= start_date:
            validation_error["end_date"] = "The end date must be after the start date."

        num_volunteers = attendees_qs.filter(volunteer__isnull=False).count()
        max_volunteers = attrs.get("max_volunteers")

        if max_volunteers < num_volunteers:
            validation_error[
                "max_volunteers"
            ] = "The max number of volunteers must be higher or equal to the number of volunteers selected."

        if validation_error:
            raise serializers.ValidationError(validation_error)

        return attrs
