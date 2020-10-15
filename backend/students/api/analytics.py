from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from students.services import student_analytics


class StudentGeneralAnalytics(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response(student_analytics())
