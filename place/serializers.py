from .models import Place
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ("name", "address")
        
