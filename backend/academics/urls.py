from rest_framework import routers

from .api import ClassesViewSet, ClassNumeralViewSet, StreamViewSet, ClassesNSViewSet, SubjectViewSet

router = routers.DefaultRouter()
router.register("api/v2.0/academics/classes", ClassesViewSet, "Classes")
router.register("api/v2.0/academics/classesNS", ClassesNSViewSet, "ClassesNS")
router.register("api/v2.0/academics/classNumeral", ClassNumeralViewSet, "ClassNumeral")
router.register("api/v2.0/academics/stream", StreamViewSet, "Stream")
router.register("api/v2.0/academics/subject", SubjectViewSet, "Subject")

urlpatterns = router.urls
