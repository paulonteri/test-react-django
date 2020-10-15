from django.db import models

from academics.models import Subject
from students.models import Student


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100, blank=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the Book", blank=True)
    ISBN = models.CharField('ISBN', max_length=13, blank=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    type = models.CharField(max_length=100, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, help_text='Select Subject', null=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
        # include author

    # def get_absolute_url(self):
    #     return reverse("book_detail", args=[str(self.id)])

    # def display_author_fn(self):
    #     return ','.join(i.first_name for i in self.author.all()[:3])

    # def display_author_ln(self):
    #     return ','.join(i.last_name for i in self.author.all()[:3])


class BookInstance(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now_add=True)
    time_last_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.book.title}, ID:{self.id}'

    # def __str__(self):
    #     return f'{self.book.title}{self.student.student_id}: {self.student.first_name} {self.student.first_name} '

    # String for representing the Model Object

    # The model __str__() represents the BookInstance object
    # using a combination of its unique id and the associated Book's title.

    # f-strings
    # f'{self.id} ({self.book.title})'

    # class Meta:
    #     ordering = ["date_due_back"]


class IssueBook(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(BookInstance, on_delete=models.PROTECT)
    time_added = models.DateTimeField(auto_now_add=True, null=True)
    time_last_edited = models.DateTimeField(auto_now=True, null=True)
    available = models.BooleanField(default=False)
