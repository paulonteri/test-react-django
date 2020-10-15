import json

from rest_framework import serializers
import json
from django.core import serializers as ser

from .models import Assignment, AssignmentSubmission, AssignmentMarks, AssignmentClass


class AssignmentSerializer(serializers.ModelSerializer):
    classes_involved = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Assignment
        fields = ['id', 'name', 'description', 'time_starts', 'time_required', 'file1', 'file2', 'file3',
                  'time_last_edited', 'time_added', 'parents_notified', 'classes_involved']

    def get_classes_involved(self, obj):
        return AssignmentClass.objects.filter(assignment=obj.id).values()


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = ['id', 'student', 'assignment', 'description', 'file1', 'file2', 'file3', 'time_last_edited',
                  'time_added']


class AssignmentMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentMarks
        fields = ['id', 'assignment_submitted', 'marks', 'comments', 'time_last_edited',
                  'time_added']


class AssignmentClassSerializer(serializers.ModelSerializer):
    assignment_description = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AssignmentClass
        fields = ['id', 'assignment', 'class_ns', 'time_last_edited',
                  'time_added', 'assignment_description']

    def get_assignment_description(self, obj):
        return ser.serialize('python', [obj.assignment, ])[0]['fields']


# TODO: Create Function that returns the totals per year for a given model and field
# x = Assignment.objects.values(
#     'time_added__day').order_by('time_added__day').annotate(T=Count('pk'))

# x = AssignmentMarks.objects.values(
#     'time_added__day').order_by('time_added__day').annotate(T=Sum('marks'))
