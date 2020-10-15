from rest_framework import serializers

from .models import Classes, ClassNumeral, Stream, Subject


# Class Numeral
class ClassNumeralSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassNumeral
        fields = "__all__"


# Stream
class StreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stream
        fields = "__all__"


# Classes Serializer
class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = "__all__"


# ClassesNS Serializer


class ClassesNSSerializer(serializers.ModelSerializer):
    # using drf-writable-nested
    class_numeral = ClassNumeralSerializer(allow_null=True)
    stream = StreamSerializer(allow_null=True)

    class Meta:
        model = Classes
        fields = "__all__"


# Subject
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"
