from rest_framework import serializers
from .models import BookItem, Book


class BookSerializer(serializers.ModelSerializer):
   class Meta:
      model = Book
      fields = "__all__"

class BookItemSerializer(serializers.ModelSerializer):
   class Meta:
      model = BookItem
      fields = "__all__"
