from django.urls import path, include
from rest_framework import routers

from students.api.analytics import StudentGeneralAnalytics
from students.api.api import StudentViewSet, DormitoriesViewSet

router = routers.DefaultRouter()
router.register("api/v2.0/students/students", StudentViewSet, "Students")
router.register("api/v2.0/dormitories", DormitoriesViewSet, "Dormitories")
# router.register("api/v2.0/studentsdetailed",
#                 StudentDetailedSerializer, "Students Detailed")  ## ERROR


urlpatterns = router.urls

urlpatterns = [
    path('api/v2.0/students/analytics/general',
         StudentGeneralAnalytics.as_view(), name='Students Analytics'),
    path('', include(router.urls)),

]
