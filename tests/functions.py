import unittest

from answers import functions

from helpers.exec_time import ExecTimer

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

    def test_get_fibonacci_number(self):
        """
        You need to return number on n's position of fibonacci sequence
        """
        self.assertEqual(functions.get_fibonacci_number(5), 5)
        self.assertEqual(functions.get_fibonacci_number(10), 55)

    def test_cached_function(self):
        """
        You need to create function with cached calculations
        """
        timer = ExecTimer()

        functions.cached_calculations(functions.get_fibonacci_number, 27)
        time_1 = timer.getvalue()

        timer.reset()

        functions.cached_calculations(functions.get_fibonacci_number, 27)
        time_2 = timer.getvalue()

        time_ratio = (time_2/time_1)*100

        # second function call must be at least 99% faster than first call
        self.assertTrue(time_ratio < 1, "Function runs too long, seems no caching")