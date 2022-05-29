from django.db import models
from place.models import Place
from core.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.


class Rack(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4())
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.uuid} | {self.place.name}"

    @property
    def name_uuid(self) -> dict:
        return {
            "numer": self.number,
            "id": self.uuid
        }


class Book(models.Model):

    GENRE_BOOKS_CHOICES = [
        ("c", "Science"),
        ("h", "History"),
        ("h", "Horror"),
        ("f", "Fiction"),
        ("r", "Romace"),
        ("l", "Literature"),
        ("r", "Romace"),
        ("l", "Literature"),
        ("t", "Technology"),

    ]

    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    available = models.IntegerField()
    author = models.CharField(max_length=150)
    pages = models.IntegerField()
    genre = models.CharField(choices=GENRE_BOOKS_CHOICES, max_length=1)

    def __str__(self):
        return f"{self.title} | {self.rack.uuid} | {self.available}"


class BookItem(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4())
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
    is_rent = models.BooleanField(default=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.book.title}  "

