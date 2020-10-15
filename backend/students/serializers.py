from drf_writable_nested.serializers import WritableNestedModelSerializer
from rest_framework import serializers

from academics.serializers import ClassesSerializer
from .models import Student, Dormitories


# Dormitories Serializer
class DormitoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dormitories
        fields = "__all__"


# Student Detailed Serializer
class StudentDetailedSerializer(WritableNestedModelSerializer):
    # using drf-writable-nested
    class_ns = ClassesSerializer(allow_null=True)
    dormitory = DormitoriesSerializer(allow_null=True)

    class Meta:
        model = Student
        fields = "__all__"


# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
