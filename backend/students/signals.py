from django.db.models.signals import post_save, post_delete
from .models import Student


def add_student(sender, **kwargs):
    pass


post_save.connect(add_student, sender=Student)
post_delete.connect(add_student, sender=Student)
