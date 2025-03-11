from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    # Custom validation for ensuring the publication year is not in the future
    def validate_publication_year(self, value):
        if value > 2025:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    # Nested BookSerializer to display all books related to an author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

