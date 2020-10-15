from rest_framework import viewsets, permissions

from examinations.models import Exam
from examinations.serializers import ExamSerializer


class ExamsAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
