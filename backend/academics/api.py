from rest_framework import viewsets, permissions

from .models import ClassNumeral, Stream, Classes, Subject
from .serializers import ClassNumeralSerializer, StreamSerializer, ClassesSerializer, ClassesNSSerializer, \
    SubjectSerializer


# Class Numeral ViewSet
class ClassNumeralViewSet(viewsets.ModelViewSet):
    queryset = ClassNumeral.objects.all()
    serializer_class = ClassNumeralSerializer
    permission_classes = [permissions.DjangoModelPermissions]


# Stream ViewSet
class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer
    permission_classes = [permissions.DjangoModelPermissions]


# Classes ViewSet
class ClassesViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    permission_classes = [permissions.DjangoModelPermissions]


# Classes ViewSet
class ClassesNSViewSet(viewsets.ModelViewSet):
    queryset = Classes.objects.all()
    serializer_class = ClassesNSSerializer
    permission_classes = [permissions.DjangoModelPermissions]


# Subject ViewSet
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.DjangoModelPermissions]
