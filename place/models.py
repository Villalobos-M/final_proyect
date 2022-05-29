from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name_address

    @property
    def name_address(self) -> str:
        return f"{self.name} | {self.address}"
