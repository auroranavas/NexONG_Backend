from nexong.models import User
from rest_framework.serializers import ModelSerializer
from nexong.models import Meeting


class MeetingSerializer(ModelSerializer):
    class Meta:
        model = Meeting
        fields = "__all__"
