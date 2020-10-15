# from django.conf import settings # TODO:CACHE
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
import json

from cacheops import cached_view_as
from django.utils.decorators import method_decorator
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError

from academics.models import Classes
from .models import Assignment, AssignmentSubmission, AssignmentMarks, AssignmentClass
from .serializers import AssignmentSerializer, AssignmentSubmissionSerializer, \
    AssignmentMarksSerializer, AssignmentClassSerializer


# CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


class AssignmentAPI(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.AllowAny]

    classes = None

    def create(self, request, *args, **kwargs):
        try:
            self.classes = json.loads(request.data.__getitem__("classes_involved"))
            if len(self.classes) < 1:
                raise ValidationError({
                    "classes": [
                        "This field is required."
                    ]
                })
        except Exception:
            raise ValidationError({
                "classes": [
                    "This field is required."
                ]
            })

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        print("classes", self.classes)
        if len(self.classes) > 0:
            for q in self.classes:
                print(q)
                obj = AssignmentClass(class_ns=Classes.objects.get(pk=q),
                                      assignment=Assignment.objects.get(pk=instance.id))
                obj.save()
                print("id", obj.id)

        super().perform_create(serializer)

    @method_decorator(cached_view_as(Assignment.objects.all()))
    def dispatch(self, *args, **kwargs):
        return super(AssignmentAPI, self).dispatch(*args, **kwargs)

    # # @method_decorator(cache_page(CACHE_TTL))
    # def retrieve(self, request, *args, **kwargs):
    #     return super().retrieve(request, *args, **kwargs)
    #
    # # @method_decorator(cache_page(CACHE_TTL))
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)

    # @action(detail=True)
    # def classes_set(self, request, pk=None):
    #     # Get labelset id
    #     ls = AssignmentClass.objects.get(pk=pk).labelset
    #
    #     # Get LabelSet instance
    #     serializer = AssignmentClassSerializer(data=model_to_dict(ls))
    #     if serializer.is_valid():
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# UPLOAD LIST

# class AssignmentFileAPI(viewsets.ModelViewSet):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = AssignmentFileSerializer
#     queryset = AssignmentFile.objects.all()

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED,
#                         headers=headers)


class AssignmentSubmissionAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssignmentSubmissionSerializer
    queryset = AssignmentSubmission.objects.all()


class AssignmentMarksAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssignmentMarksSerializer
    queryset = AssignmentMarks.objects.all()


class AssignmentClassAPI(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = AssignmentClassSerializer
    queryset = AssignmentClass.objects.all()
