"""With this string:
'monty pythons flying circus'

Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'

Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']

Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

Created on 3 Nov 2015

@author: paulross
"""
import unittest


def no_duplicates(a_string):
    return "".join(sorted(set(a_string)))


def reversed_words(a_string):
    return a_string.split(" ")[::-1]


def four_char_strings(a_string):
    return [a_string[0 + i:4 + i] for i in range(0, len(a_string), 4)]


class TestStrings(unittest.TestCase):
    def test_no_duplicates(self):
        s = 'monty pythons flying circus'
        self.assertEqual(no_duplicates(s), ' cfghilmnoprstuy')

    def test_reversed_words(self):
        s = 'monty pythons flying circus'
        self.assertEqual(reversed_words(s), ['circus', 'flying', 'pythons', 'monty'])

    def test_four_char_strings(self):
        s = 'monty pythons flying circus'
        self.assertEqual(four_char_strings(s), ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus'])
