from unittest import TestCase
# from django.test import TestCase
from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)

    def test_minus(self):
        result = operations(6, 13, '-')
        self.assertEqual(-7, result)

    def test_mult(self):
        result = operations(6, 13, '*')
        self.assertEqual(78, result)

    def test_div(self):
        result = operations(26, 13, '/')
        self.assertEqual(2, result)
