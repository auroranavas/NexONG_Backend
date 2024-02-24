from rest_framework import serializers
from nexong.models import Event, User
from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    educators = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.filter(educator__isnull=False))
    
    class Meta:
        model = Event
        fields = ['name','description','place','capacity','max_volunteers',
        'start_date','end_date','lesson', 'educators']

    def get_educators(self, obj):
        educators = User.objects.filter(educator__isnull=False)
        return educators

    def validate_educators(self, value):
        if not value:
            raise serializers.ValidationError("Must provide at least 1 educator.")
        return value
