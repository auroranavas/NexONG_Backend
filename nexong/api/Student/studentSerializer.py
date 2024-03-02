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

        def validation_error(title="Error"):
            raise serializers.ValidationError(title)

        def validate(self, data):
            if data["name"] == "":
                self.validation_error("Name can't be empty")

            if data["surname"] == "":
                self.validation_error("Surname can't be empty")

            if data["birthdate"] > datetime.date.today():
                self.validation_error("Birthdate can't be greater than today")

            return data
