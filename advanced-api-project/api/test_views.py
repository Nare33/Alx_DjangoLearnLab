# advanced-api-project/api/test_views.py
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

class BookAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.book1 = Book.objects.create(title='Test Book 1', author='Author 1', publication_date='2023-01-01')
        self.book2 = Book.objects.create(title='Test Book 2', author='Author 2', publication_date='2023-02-01')

    def test_book_list(self):
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_detail(self):
        response = self.client.get(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')

    def test_book_create(self):
        data = {'title': 'New Book', 'author': 'New Author', 'publication_date': '2023-03-01'}
        response = self.client.post(reverse('book-list'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(title='New Book').author, 'New Author')

    def test_book_update(self):
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_date': '2023-04-01'}
        response = self.client.put(reverse('book-detail', args=[self.book1.id]), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book1.id).title, 'Updated Book')

    def test_book_delete(self):
        response = self.client.delete(reverse('book-detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_filter(self):
        response = self.client.get(reverse('book-list') + '?author=Author 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_book_search(self):
        response = self.client.get(reverse('book-list') + '?search=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_ordering(self):
        response = self.client.get(reverse('book-list') + '?ordering=publication_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 1') #Earlier date should be first.

        response = self.client.get(reverse('book-list') + '?ordering=-publication_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')#Later date should be first.

    def test_unauthenticated_access(self):
        self.client.credentials() # Remove credentials
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
