from datetime import datetime
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from nexong.models import EducationCenter, Family, Student


class StudentSerializer(ModelSerializer):
    education_center = serializers.PrimaryKeyRelatedField(
        many=False, required=True, queryset=EducationCenter.objects.all()
    )
    family = serializers.PrimaryKeyRelatedField(
        many=False, required=True, queryset=Family.objects.all()
    )

    class Meta:
        model = Student
        fields = [
            "id",
            "name",
            "surname",
            "current_education_year",
            "education_center_tutor",
            "enrollment_document",
            "scanned_sanitary_card",
            "nationality",
            "birthdate",
            "is_morning_student",
            "status",
            "activities_during_exit",
            "education_center",
            "family",
        ]

        def validate(self, data):
            if data["name"] == "":
                raise serializers.ValidationError("Name can't be empty")

            if data["surname"] == "":
                raise serializers.ValidationError("Surname can't be empty")

            if data["birthdate"] > datetime.date.today():
                raise serializers.ValidationError(
                    "Birthdate can't be greater than today"
                )

            return data
