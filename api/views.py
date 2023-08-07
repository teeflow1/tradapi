from django.shortcuts import render
from book.models import Book
from api.serializers import Bookserializer
from rest_framework import generics


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

