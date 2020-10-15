from django.db import models

from academics.models import Subject
from students.models import Student


class Exam(models.Model):
    name = models.CharField(max_length=255)
    exam_start_date = models.DateField()
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.exam_start_date})'

    class Meta:
        ordering = ['exam_start_date', 'name']


class ExamResults(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    marks = models.IntegerField()

    def __str__(self):
        return f'{self.student} ({self.exam.name})'

    class Meta:
        ordering = ['student', 'subject']
        unique_together = ['exam', 'student', 'subject']
