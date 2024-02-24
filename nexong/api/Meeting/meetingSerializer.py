from rest_framework import serializers
from nexong.models import User
from rest_framework.serializers import ModelSerializer
from nexong.models import Meeting


class MeetingSerializer(ModelSerializer):
    attendees = serializers.PrimaryKeyRelatedField(
        many=True, queryset=User.objects.filter(student__isnull=False)
    )

    class Meta:
        model = Meeting
        fields = ["name", "description", "date", "time", "attendees"]
