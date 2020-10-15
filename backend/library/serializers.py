from rest_framework import serializers

from .models import Book, BookInstance, IssueBook


# Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


# Book Instance
class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = "__all__"


# Book Instance
class IssueBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueBook
        fields = "__all__"
