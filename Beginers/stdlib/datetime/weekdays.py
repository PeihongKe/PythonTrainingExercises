"""Create a function that returns a list of a given size of date objects
that correspond to week days starting at a given date.

Created on 17 Feb 2016

@author: paulross
"""
import datetime

import unittest


def business_days(start_date, num):
    start_date


class TestWeekdays(unittest.TestCase):
    def test_business_days(self):
        start_date = datetime.date(2016, 1, 1)
        result = business_days(start_date, 10)
        expected = [
            datetime.date(2016, 1, 1),
            datetime.date(2016, 1, 4),
            datetime.date(2016, 1, 5),
            datetime.date(2016, 1, 6),
            datetime.date(2016, 1, 7),
            datetime.date(2016, 1, 8),
            datetime.date(2016, 1, 11),
            datetime.date(2016, 1, 12),
            datetime.date(2016, 1, 13),
            datetime.date(2016, 1, 14),
        ]
        self.assertEqual(result, expected)
