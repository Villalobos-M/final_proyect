from django.shortcuts import render
from rest_framework import viewsets
from book.models import BookItem, Book
from book.serializers import BookItemSerializer, BookSerializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class BookViewset(viewsets.ModelViewSet):
   queryset = Book.objects.all()
   serializer_class = BookSerializer
   filter_backends = [DjangoFilterBackend, filters.SearchFilter]
   filterset_fields = ['title', 'author', 'genre']
   search_fields = ['author']


class BookItemViewset(viewsets.ModelViewSet):
   queryset = BookItem.objects.all()
   serializer_class = BookItemSerializer
