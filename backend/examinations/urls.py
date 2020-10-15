from django.urls import path, include
from rest_framework import routers

from examinations.api.fetch import GetAllExamResultsAPI, GetStudentResultsAPI, GetClassPerExamResultsAPI
from examinations.api.general import ExamsAPI
from examinations.api.save import SavePerStudentExamResultsAPI, SavePerClassExamResultsAPI

router = routers.DefaultRouter()
router.register('api/v2.0/exams/exams', ExamsAPI, 'Exams')

urlpatterns = [
    path('api/v2.0/exams/results/get/all/', GetAllExamResultsAPI.as_view(), name='Get All Exam results'),
    path('api/v2.0/exams/results/get/student/<int:pk>/', GetStudentResultsAPI.as_view(), name='Get Student results'),
    path('api/v2.0/exams/results/get/class/<int:classs>/subject/<int:subject>/', GetClassPerExamResultsAPI.as_view(),
         name='Get Per Class Per Exam results'),
    path('api/v2.0/exams/results/save/student/', SavePerStudentExamResultsAPI.as_view(), name='Save Exam results '
                                                                                              'Per Student'),
    path('api/v2.0/exams/results/save/class/', SavePerClassExamResultsAPI.as_view(), name='Save Exam results '
                                                                                          'Per Class'),
    path('', include(router.urls)),

]
