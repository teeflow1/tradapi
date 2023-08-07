from rest_framework import serializers
from book.models import Book

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'author', 'isbn')