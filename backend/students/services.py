from cacheops import cached_as
from django.db.models import Count

from students.models import Student


@cached_as(Student.objects.all())
def student_analytics():
    """
    General student analytics
    """
    total_students = Student.objects.count()
    female = Student.objects.filter(gender="f").count()
    male = Student.objects.filter(gender="m").count()
    religion = Student.objects.values('religion').order_by('religion').annotate(Total=Count('pk'))
    students_per_class = Student.objects.values('class_ns', 'class_ns__class_numeral', 'class_ns__stream').order_by(
        'class_ns').annotate(Total=Count('pk'))
    students_per_class_numeral = Student.objects.values('class_ns__class_numeral').order_by(
        'class_ns__class_numeral').annotate(Total=Count('pk'))
    students_per_year = Student.objects.values('admission_date__year').order_by('admission_date__year').annotate(
        Total=Count('pk'))
    dormitory = Student.objects.values('dormitory', 'dormitory__dormitory_name').order_by('dormitory').annotate(
        Total=Count('pk'))

    response_data = {
        "total_students": total_students,
        "female": female,
        "male": male,
        "students_per_class": students_per_class,
        "students_per_class_numeral": students_per_class_numeral,
        "students_per_year": students_per_year,
        "religion": religion,
        "dormitory": dormitory
    }
    return response_data
