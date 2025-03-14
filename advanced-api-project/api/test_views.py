from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        # Create a user for authentication
        cls.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create some books in the database
        cls.book1 = Book.objects.create(title="Book One", author="Author One", publication_date="2023-01-01")
        cls.book2 = Book.objects.create(title="Book Two", author="Author Two", publication_date="2022-01-01")

    def test_create_book(self):
        """Test creating a new book."""
        url = reverse('book-list')  # Make sure you use the correct URL name for the Book list view
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'publication_date': '2024-01-01'
        }

        # Test with authentication
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

    def test_read_books(self):
        """Test reading the list of books."""
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # There should be 2 books in the database

    def test_update_book(self):
        """Test updating a book."""
        url = reverse('book-detail', args=[self.book1.id])  # Ensure you use the correct URL pattern
        data = {
            'title': 'Updated Book One',
            'author': 'Updated Author One',
            'publication_date': '2025-01-01'
        }
        self.client.login(username='testuser', password='testpassword')
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Book One')

    def test_delete_book(self):
        """Test deleting a book."""
        url = reverse('book-detail', args=[self.book1.id])
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Try fetching the book again to ensure it's deleted
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_filter_books(self):
        """Test filtering books by author."""
        url = reverse('book-list') + '?author=Author One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author One')

    def test_order_books(self):
        """Test ordering books by publication date."""
        url = reverse('book-list') + '?ordering=publication_date'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book Two')  # 'Book Two' should be first

    def test_search_books(self):
        """Test searching books by title."""
        url = reverse('book-list') + '?search=Book One'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_permission_required_for_delete(self):
        """Test that only authorized users can delete books."""
        url = reverse('book-detail', args=[self.book1.id])
        # Without login
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Login as an admin user
        admin_user = User.objects.create_superuser(username='admin', password='adminpassword')
        self.client.login(username='admin', password='adminpassword')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

