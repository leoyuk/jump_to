import json
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'id' : 9999,
            'author' : {
                'id' : 9999,
                'name' : 'tester',
                'age' : 45,
            },
            'title' : 'TEST BOOK',
            'published_date' : '2024-06-13',
            'price' : "15000000",
        }
        self.book = Book.objects.create(self.book_data)

    def test_get_all_books(self):
        response = self.client.get('/example_app/api/books/')
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data) # Check 'results' Key

    def test_get_single_book(self):
        response = self.client.get(f'/example_app/api/books/{self.book.id}')
        book = Book.objects.get(id=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        response = self.client.post('/example_app/api/books/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        updated_data = {
            'id' : 99998,
        }
        response = self.client.put(f'/exmaple_app/api/books/{self.book.id}', data=updated_data, format ='json')