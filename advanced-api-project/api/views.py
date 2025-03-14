from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters import FilterSet, CharFilter, NumberFilter

class BookFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains')  
    author = CharFilter(lookup_expr='icontains')
    publication_year = NumberFilter(field_name='publication_date', lookup_expr='year')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_date']  
    ordering = ['title']  

