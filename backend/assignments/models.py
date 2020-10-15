from django.db import models

from academics.models import Classes
from students.models import Student


class Assignment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    file1 = models.FileField(
        upload_to="files/teachers/assignments", null=True, blank=True)
    file2 = models.FileField(
        upload_to="files/teachers/assignments", null=True, blank=True)
    file3 = models.FileField(
        upload_to="files/teachers/assignments", null=True, blank=True)
    #
    time_starts = models.DateTimeField()
    time_required = models.DateTimeField()
    parents_notified = models.BooleanField(default=False)
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["name", "time_added"]
        ordering = ['-time_last_edited', '-time_starts']

    def __str__(self):
        return f'{self.name} {self.time_starts}'


class AssignmentClass(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    class_ns = models.ForeignKey(Classes, on_delete=models.CASCADE)
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["assignment", "class_ns"]
        order_with_respect_to = 'assignment'

    def __str__(self):
        return f'{self.assignment.name}: {self.class_ns.class_numeral} {self.class_ns.stream}'


class AssignmentSubmission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    description = models.TextField()
    file1 = models.FileField(
        upload_to="files/students/assignments", null=True, blank=True)
    file2 = models.FileField(
        upload_to="files/students/assignments", null=True, blank=True)
    file3 = models.FileField(
        upload_to="files/students/assignments", null=True, blank=True)
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["assignment", "student"]
        order_with_respect_to = 'assignment'

    def __str__(self):
        return f'{self.student.student_id}: {self.assignment.name} {self.assignment.time_required}'


class AssignmentMarks(models.Model):
    assignment_submitted = models.OneToOneField(
        AssignmentSubmission, on_delete=models.CASCADE)
    marks = models.IntegerField()
    comments = models.TextField(null=True)
    #
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time_last_edited', '-marks']
        constraints = [
            models.CheckConstraint(check=models.Q(marks__lte=100), name='marks_lte_100'),
        ]

    def __str__(self):
        return f'{self.assignment_submitted.student_id}: {self.assignment_submitted.assignment.name} {self.marks}'
