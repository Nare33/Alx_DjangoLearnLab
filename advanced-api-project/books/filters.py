# filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial matching
    author = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive partial matching
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

