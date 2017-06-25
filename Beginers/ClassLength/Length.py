#!/usr/bin/env python
"""Task create a class to represent lengths.

Create a specialised exception that this module might raise on error.

This needs to define an __init__() constructor that takes a a number,
assumed to be meters

Implement __str__ to give a string representation used by str() and print

Implement a function, convert(string) that returns the value converted to 'feet', 'mm', 'inch'

Implement a function to add two classes together and return the sum as a class

STRETCH: Change the constructor so it can take a number and a string, for
example:
l = Length(21.2, "inch")
STRETCH: Change the function that adds two classes together to be more flexible
so that it can add a number to a class Length returning a class Length.
Example:
l = Length(23)
m = l + 21


Created on Sep 12, 2011

@author: paulross
"""

__author__ = 'Paul Ross'
__date__ = '2011-08-03'
__version__ = '0.1.0'
__rights__ = 'Copyright (c) 2011 Paul Ross. Copyright (c) 2015 AHL.'

import unittest

import pytest


# Create a specialised exception called ExceptionLength that we can use on error.

# Fill in the functions that Length needs.
class Length(object):
    """Class that represents length. Constructor takes a number represents
    metres."""

    def __init__(self, value_in_m):
        self.value = value_in_m

    def __str__(self):
        return 'Length: %.3f (m)' % self.value

    def convert(self, uom):
        if uom == "mm":
            return 1000 * self.value
        elif uom == "cm":
            return 100 * self.value
        else:
            raise ExceptionLength('Can not convert to: %s' % uom)

    # Create the appropriate function to add two Length classes together
    def __add__(self, other):
        return Length(self.value + other.value)


class ExceptionLength(Exception):
    pass


class TestLength(unittest.TestCase):
    def test_convert(self):
        length = Length(12)
        self.assertEqual(12000, length.convert('mm'))

    def test_str(self):
        length = Length(12.5)
        self.assertEqual('Length: 12.500 (m)', str(length))

    def test_convert_raises(self):
        length = Length(12.5)
        with pytest.raises(ExceptionLength) as err:
            length.convert('miles')
        self.assertEqual('Can not convert to: miles', err.value.args[0])

    def test_add(self):
        len_a = Length(2)
        len_b = Length(6)
        len_total = len_a + len_b
        self.assertEqual(8, len_total.value)
