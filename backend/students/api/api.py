from cacheops import cached_view_as
from django.utils.decorators import method_decorator
from rest_framework import viewsets, permissions

from students.models import Student, Dormitories
from students.serializers import StudentSerializer, DormitoriesSerializer, StudentDetailedSerializer


# Students View
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    @method_decorator(cached_view_as(Student))
    def dispatch(self, *args, **kwargs):
        return super(StudentViewSet, self).dispatch(*args, **kwargs)


# Students View
class StudentDetailedViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentDetailedSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    @method_decorator(cached_view_as(Student))
    def dispatch(self, *args, **kwargs):
        return super(StudentDetailedViewSet, self).dispatch(*args, **kwargs)


# Dormitories View
class DormitoriesViewSet(viewsets.ModelViewSet):
    queryset = Dormitories.objects.all()
    serializer_class = DormitoriesSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    @method_decorator(cached_view_as(Dormitories))
    def dispatch(self, *args, **kwargs):
        return super(DormitoriesViewSet, self).dispatch(*args, **kwargs)
