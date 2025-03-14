from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    author = filters.CharFilter(lookup_expr='icontains')
    publication_date = filters.DateFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']
