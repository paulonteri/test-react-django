from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from examinations.services.save import save_results_per_student, save_results_per_subject


class SavePerStudentExamResultsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        return Response(save_results_per_student(
            exam=request.data['exam'], student=request.data['student'], subject_marks=request.data['subject_marks'])
        )


class SavePerClassExamResultsAPI(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        return Response(save_results_per_subject(exam=request.data['exam'], subject=request.data['subject'],
                                                 student_marks=request.data['student_marks']))
