from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_fields = ['title'] 

    # Step 1: Filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Step 2: Searching
    search_fields = ['title', 'author']

    # Step 3: Ordering
    ordering_fields = ['title', 'publication_year']
