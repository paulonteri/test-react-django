from rest_framework import serializers

from .models import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'exam_start_date']
