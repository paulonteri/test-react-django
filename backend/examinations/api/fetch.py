# TODO: Add computational intensive tasks to cache
# https://code.tutsplus.com/tutorials/how-to-cache-using-redis-in-django-applications--cms-30178
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from examinations.services.fetch import all_exam_results, per_student_results, per_class_per_subject_results


class GetAllExamResultsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response(all_exam_results())


class GetStudentResultsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        return Response(per_student_results(pk))


class GetClassPerExamResultsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, classs, subject, format=None):
        return Response(per_class_per_subject_results(classs, subject))
