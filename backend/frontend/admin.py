from django.contrib import admin

from academics.models import Subject, ClassNumeral, Stream, Classes, SubjectTeacherClass, ExamPerformance, Club
from examinations.models import Exam, ExamResults
# from school.models import SchoolInfo, FeePayable, FeePaymentStatus
from library.models import Book, BookInstance, IssueBook
from staff.models import Staff, StaffRole, TeachingStaff
from students.models import Student, DisciplinaryIssue, HealthIssue, Dormitories
from assignments.models import Assignment, AssignmentSubmission,  AssignmentMarks, AssignmentClass

# Register your models here.

# @admin.register(StaffRole)

admin.site.register(Staff)
admin.site.register(StaffRole)
admin.site.register(TeachingStaff)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(ClassNumeral)
admin.site.register(Stream)
admin.site.register(Classes)
# admin.site.register(SchoolInfo)
# admin.site.register(FeePayable)
# admin.site.register(FeePaymentStatus)
admin.site.register(Club)
admin.site.register(BookInstance)
admin.site.register(Book)
admin.site.register(IssueBook)
admin.site.register(DisciplinaryIssue)
admin.site.register(HealthIssue)
admin.site.register(Dormitories)
admin.site.register(SubjectTeacherClass)
admin.site.register(Exam)
admin.site.register(ExamResults)
admin.site.register(Assignment)
admin.site.register(AssignmentClass)

admin.site.register(AssignmentSubmission)

admin.site.register(AssignmentMarks)

#####################################

# list view

# @admin.register(BookAdmin)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')  # fields to be displayed
#     fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]  # how they are displayed
#     list_filter = ('status', 'due_back')  # filter(on the side)

######################################

# detail view (sectioned)

# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('status', 'due_back')
#
#     fieldsets = (
#         (None, {
#             'fields': ('book', 'imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back')
#         }),
#     )

#####################################

# Inline editing of associated records

# class BooksInstanceInline(admin.TabularInline):
#     model = BookInstance
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'display_genre')
#     inlines = [BooksInstanceInline]

##########################################################################

# Unfortunately we can't directly specify the genre field in list_display because it is a ManyToManyField (Django
# prevents this because there would be a large database access "cost" in doing so). Instead we'll define a
# display_genre function to get the information as a string (this is the function we've called above; we'll define it
# below).

# def display_genre(self):
#     """Create a string for the Genre. This is required to display genre in Admin."""
#     return ', '.join(genre.name for genre in self.genre.all()[:3])
#
#
# display_genre.short_description = 'Genre'
