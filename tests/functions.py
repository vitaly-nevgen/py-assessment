import unittest

from answers import functions


class FunctionsTestCase(unittest.TestCase):

    def test_parse_arguments(self):
        """
        You should return dictionary containing arguments which was passed to function
        """
        result = functions.parse_arguments(1, 2, 5)
        self.assertEqual(result, {"args": (1, 2, 5)})

        result = functions.parse_arguments(spam='foo', eggs='bar')
        self.assertEqual(result, {"kwargs": {"spam": 'foo', "eggs": 'bar'}})

        result = functions.parse_arguments(5, 6, test=1)
        self.assertEqual(result, {"args": (5, 6), "kwargs": {"test": 1}})

    def test_decorator(self):
        """
        You need to create function which returns decorator making function output bold
        Example: return 'abc' --> '<b>abc</b>'
        """
        wrapper = functions.get_bold_decorator()

        @wrapper
        def test_func(string):
            return string

        self.assertEqual(test_func('Hello'), '<b>Hello</b>')
        self.assertEqual(test_func('Hello, World!'), '<b>Hello, World!</b>')