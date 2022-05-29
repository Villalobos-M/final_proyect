from django.shortcuts import render
from .models import Place
from rest_framework import viewsets
from .serializers import UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Place.objects.all()
