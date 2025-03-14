from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework as filters

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']
