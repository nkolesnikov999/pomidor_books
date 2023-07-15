from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Book test1', price=25, author_name='author 1')
        book_2 = Book.objects.create(name='Book test2', price=55, author_name='author 2')
        data = BookSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Book test1',
                'price': '25.00',
                'author_name': 'author 1',
            },
            {
                'id': book_2.id,
                'name': 'Book test2',
                'price': '55.00',
                'author_name': 'author 2',
            }
        ]
        self.assertEqual(expected_data, data)
