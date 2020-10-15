from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from academics.models import Classes


class Dormitories(models.Model):
    dormitory_name = models.CharField(max_length=50, unique=True)
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.dormitory_name}'


def validate_phone_length(value):
    if len(value) < 13 or len(value) > 13:
        raise ValidationError(
            _('%(value)s is not a correct phone number.'),
            params={'value': value},
        )


class Student(models.Model):
    student_id = models.IntegerField(
        primary_key=True, help_text="Enter Student ID")
    class_ns = models.ForeignKey(Classes, null=True, on_delete=models.PROTECT)
    dormitory = models.ForeignKey(
        Dormitories, on_delete=models.PROTECT, null=True)
    first_name = models.CharField(max_length=50, help_text="Enter First Name")
    surname = models.CharField(max_length=50, help_text="Enter Family Name")
    other_name = models.CharField(
        max_length=50, help_text="Enter Other Name", blank=True)
    student_email = models.EmailField(blank=True, null=True)
    student_phone = models.CharField(max_length=13, validators=[
        validate_phone_length], null=True, blank=True, )
    father_alive = models.BooleanField(default=True, blank=True,
                                       help_text="Is the father alive?")
    mother_alive = models.BooleanField(
        default=True, blank=True, null=True,
        help_text="Is the mother alive?")
    father_first_name = models.CharField(max_length=50, blank=True, help_text="Enter the first name of the student's "
                                                                              "male guardian")
    father_surname = models.CharField(max_length=50, blank=True)
    father_email = models.EmailField(blank=True)
    father_phone = models.CharField(max_length=13, validators=[
        validate_phone_length], null=True)
    father_premium = models.BooleanField(
        default=False, blank=True, help_text="Do not edit this")
    mother_first_name = models.CharField(max_length=50, blank=True, help_text="Enter the first name of the student's "
                                                                              "female guardian")
    mother_surname = models.CharField(max_length=50, blank=True)
    mother_email = models.EmailField(null=True)
    mother_phone = models.CharField(max_length=13, validators=[
        validate_phone_length], null=True)
    mother_premium = models.BooleanField(
        default=False, blank=True, help_text="Do not edit this")
    date_of_birth = models.DateField(blank=True)
    GENDER_CHOICES = [
        ('m', 'male'),
        ('f', 'female')]
    gender = models.CharField(
        max_length=50, choices=GENDER_CHOICES, blank=True)
    admission_date = models.DateField(null=True, blank=True, auto_now=True)
    home_country = models.CharField(
        max_length=50, blank=True, help_text="Enter home County")
    home_county = models.CharField(
        max_length=50, blank=True, help_text="Enter home County")
    home_town = models.CharField(
        max_length=50, blank=True, help_text="Enter home Town")
    religion = models.CharField(max_length=100, blank=True, null=True)
    health = models.TextField(max_length=1000, blank=True, default="Good", help_text="Enter health status "
                                                                                     "or complications")
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)
    is_enrolled = models.BooleanField(
        default=True, help_text="Is the student enrolled?")
    is_graduated = models.BooleanField(
        default=False, help_text="Has the student graduated?")

    def __str__(self):
        return f'{self.student_id}: {self.surname} {self.first_name}'

    class Meta:
        ordering = ['student_id', 'surname', 'first_name']
        # TODO: Find way to ensure that a parent's email/phone is not equal to the student's
        # unique_together = [['student_email', 'father_email'], ['student_email', 'mother_email'],
        #                    ['father_email', 'mother_email'],
        #                    ['student_phone', 'father_phone'], [
        #                        'student_phone', 'mother_phone'],
        #                    ['father_phone', 'mother_phone']]

    def get_absolute_url(self):
        reverse('student_detail', args=[str(self.student_id)])

    # def display_Class(self):                # Class from students model
    #     return ','.join(i.Class.stream for i in self.Class.all()[:3])


class DisciplinaryIssue(models.Model):
    date = models.DateField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    issue = models.TextField(max_length=300)
    outcome = models.TextField(max_length=150, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.student}'

    class Meta:
        ordering = ['date', 'student']

    def get_absolute_url(self):
        reverse('Discipline', args=[str(self.title)])


class HealthIssue(models.Model):
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    issue = models.TextField(max_length=150)
    treatment = models.TextField(max_length=150, blank=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}: {self.student}'

    class Meta:
        ordering = ['date', 'student']

    def get_absolute_url(self):
        reverse('Health', args=[str(self.title)])
