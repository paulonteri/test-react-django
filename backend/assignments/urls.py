from rest_framework import routers

from .api import AssignmentAPI, AssignmentSubmissionAPI, \
    AssignmentMarksAPI, AssignmentClassAPI

router = routers.DefaultRouter()
router.register('api/v2.0/assignments/assignments', AssignmentAPI, 'Assignments')
router.register('api/v2.0/assignments/submit/assignments', AssignmentSubmissionAPI, 'AssignmentSubmissions')
router.register('api/v2.0/assignments/marks', AssignmentMarksAPI, 'Assignment Marks')
router.register('api/v2.0/assignments/classes', AssignmentClassAPI, 'Assignment Class')

urlpatterns = router.urls
