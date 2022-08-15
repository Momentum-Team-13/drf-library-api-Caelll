from django.shortcuts import render
from .models import Book
from books.serializers import BookSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView
# Create your views here.

class BookListView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
