from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_class = Bookfilter
    
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

