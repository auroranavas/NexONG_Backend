from rest_framework import serializers
from nexong.models import *
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class EducatorSerializer(ModelSerializer):
    class Meta:
        model = Educator
        fields = "__all__"


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"


class VolunteerSerializer(ModelSerializer):
    class Meta:
        model = Volunteer
        fields = "__all__"


class FamilySerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"


class EducatorGetSerializer(ModelSerializer):
    user = UserSerializer()  # With this it brings the user related to the educator

    class Meta:
        model = Educator
        fields = "__all__"


class PartnerGetSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Partner
        fields = "__all__"


class VolunteerGetSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Volunteer
        fields = "__all__"


class FamilyGetSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Family
        fields = "__all__"
