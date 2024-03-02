from rest_framework import serializers
from nexong.models import EvaluationType, StudentEvaluation, Lesson
from rest_framework.serializers import ModelSerializer
from datetime import datetime, timezone


class StudentEvaluationSerializer(ModelSerializer):
    evaluation_type = serializers.PrimaryKeyRelatedField(
        queryset=EvaluationType.objects.all(), required=False
    )
    url = serializers.HyperlinkedIdentityField(view_name="studentevaluation-detail")

    class Meta:
        model = StudentEvaluation
        fields = [
            "id",
            "grade",
            "date",
            "comment",
            "student",
            "evaluation_type",
            "url",
            
        ]

class EvaluationTypeSerializer(ModelSerializer):
    lesson = serializers.PrimaryKeyRelatedField(
        queryset=Lesson.objects.all(), required=False
    )
    url = serializers.HyperlinkedIdentityField(view_name="evaluationtype-detail")

    class Meta:
        model = EvaluationType
        fields = [
            "id",
            "name",
            "description",
            "evaluation_type",
            "grade_system",
            "lesson",
            "url",
        ]

    