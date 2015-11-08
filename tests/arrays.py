import unittest
import sys

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

    def test_low_memory_array(self):
        """
        You need to return a low memory array or array-like object
        filled with numbers stating from zero eg. arr[50] = 50
        """
        arr = arrays.get_low_memory_array(10000)
        self.assertTrue(sys.getsizeof(arr) < 1000, "Array uses more memory than allowed")

        self.assertEqual(arr[9237], 9237)