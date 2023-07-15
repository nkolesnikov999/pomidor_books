from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from store.models import Book
from store.serializers import BookSerializer


class BookApiTestCase(APITestCase):

    def setUp(self):
        self.book_1 = Book.objects.create(name='Book test1', price=25, author_name='author1')
        self.book_2 = Book.objects.create(name='Book test2 author2', price=50, author_name='author1')
        self.book_3 = Book.objects.create(name='Book test3', price=25, author_name='author2')
        self.book_4 = Book.objects.create(name='Book test4', price=55, author_name='author1')

    def test_get(self):

        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3, self.book_4], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


    def test_get_search(self):

        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'author2'})
        serializer_data = BookSerializer([self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

