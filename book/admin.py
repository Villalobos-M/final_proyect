from django.contrib import admin
from .models import Rack, BookItem, Book
# Register your models here.

admin.site.register(Rack)
admin.site.register(BookItem)
admin.site.register(Book)