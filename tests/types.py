import unittest

from answers import types


class TypesTestCase(unittest.TestCase):

    def test_is_mutable(self):
        """
        You should determine if object is mutable
        """
        self.assertEqual(types.is_mutable((2, 3, 5)), False)
        self.assertEqual(types.is_mutable([2, 4, 5]), True)
        self.assertEqual(types.is_mutable('Hello'), False)
        self.assertEqual(types.is_mutable({}), True)

    def test_typeof(self):
        """
        You should return type string of passed object
        """
        def dummy(): pass
        lambda_func = lambda x: x*2
        elements = (1, 4, 5)
        self.assertEqual(types.typeof(dummy), 'function')
        self.assertEqual(types.typeof([1, 2, 4]), 'list')
        self.assertEqual(types.typeof(lambda_func), 'function')
        self.assertEqual(types.typeof(elements), 'tuple')