from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
from book.serializers import BookItemSerializer
from rest_framework.decorators import action
from book.models import BookItem
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    @action(detail=True)
    def my_books(self, request,  pk=None):
        queryset = BookItem.objects.filter(
            user__id=pk
        )
        serializer = BookItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
