import unittest

from answers import strings


class StringsTestCase(unittest.TestCase):

    def test_trim_string(self):
        self.assertEqual(strings.trim_string("   b"), "b")
        self.assertEqual(strings.trim_string("  \n\nv  \n\r   "), "v")
        self.assertEqual(strings.trim_string("\n\n\r   b\nc\r\n  "), "b\nc")

    def test_reverse_string(self):
        self.assertEqual(strings.reverse_string("12345"), "54321")

    def test_remove_each_2th(self):
        self.assertEqual(strings.remove_each_2th("bbcc"), "bc")
        self.assertEqual(strings.remove_each_2th("a|b|c|d|e|f"), 'abcdef')

    def test_add_zeros(self):
        self.assertEqual(strings.add_zeros(72, 2), "72")
        self.assertEqual(strings.add_zeros(10, 5), "00010")
        self.assertEqual(strings.add_zeros(100, 2), "100")

    def test_count_occurrences(self):
        self.assertEqual(strings.count_occurrences("aabbcc", "aa"), 1)
        self.assertEqual(strings.count_occurrences("aaaaaaaa", "aaaa"), 2)

    def test_string_format(self):
        result = strings.string_format("Hello {user}!", {"user": 'Vitaly'})
        self.assertEqual(result, "Hello Vitaly!")

    def test_string_format_default(self):
        string = "Player 1 is - {player1}. Player 2 is {player2}"
        params = {"player1": 'Alice'}
        default_value = "Default Player"

        result = strings.string_format(string, params, default_value)
        self.assertEqual(result, "Player 1 is - Alice. Player 2 is Default Player")