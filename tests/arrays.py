import unittest

from answers import arrays


class ArraysTestCase(unittest.TestCase):

    def test_is_elements_unique(self):
        """
        You need to check if all elements in list are unique
        """
        self.assertEqual(arrays.is_elements_unique([1, 2, 3, 4, 5]), True)
        self.assertEqual(arrays.is_elements_unique([1, 2, 2, 2, 5]), False)

    def test_remove_duplicates(self):
        """
        You need to remove duplicates from list
        """
        self.assertEqual(arrays.remove_duplicates([1, 2, 3, 5, 3]), [1, 2, 3, 5])