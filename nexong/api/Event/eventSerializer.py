from rest_framework import serializers
from nexong.models import Event, User
from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['name','description','place','capacity','max_volunteers',
        'start_date','end_date','lesson', 'educators']

