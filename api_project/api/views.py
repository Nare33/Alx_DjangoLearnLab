from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework.authtoken.views import obtain_auth_token

obtain_auth_token = obtain_auth_token

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
