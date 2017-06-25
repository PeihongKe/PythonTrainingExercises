"""Exercises with exceptions.

Exercise 1:
With the function def raise_if_not_length_four(value): check the length of
the value argument and raise an exception (specifically a ValueError) if
the length is not 4.

Exercise 2:
With the function def raise_if_not_four_characters(value): check the length of
the value argument and raise an exception (specifically a ValueError) if
the length is not 4 AND check the value is a string, if not raise, well what
would be suitable?

Exercise 3:
You need to write a function that takes an imaginary network connection (that
might be good or bad). You have some third party code that provides and data
base connection with a class DataBase. You can read data from this class but
you must always call close() before your function exits.

The problem is that if the network is bad the DataBase will raise so how do
you make sure that you always call close().

The first part of the problem is to trap the exception.
The second part of the problem is to allow the exception to propagate so that
the caller has to deal with it but you still have to call close().

Created on 3 Jan 2017

@author: paulross
"""

import unittest

import pytest


# ==== Exercise 1:
def raise_if_not_length_four(value):
    l = len(value)
    if l != 4:
        raise ValueError('Argument must be length 4, not %s' % l)
    return value


# ==== Exercise 2:
def raise_if_not_four_characters(value):
    l = len(value)
    if l != 4:
        raise ValueError('Argument must be length 4, not %s' % l)
    if not isinstance(value, str):
        raise TypeError("Argument must be a string, not %s" % type(value))
    return value


# === Exercise 3:
# ---- Regard this as third party library code that you can NOT change.
GOOD_NETWORK = 0
BAD_NETWORK = 1


class DataBase(object):
    number_of_connections = 0

    def __init__(self, network):
        self.network = network
        DataBase.number_of_connections += 1

    def read(self):
        if self.network == BAD_NETWORK:
            raise IOError('Ooops')
        return 'Data...'

    def close(self):
        DataBase.number_of_connections -= 1


def reset():
    DataBase.number_of_connections = 0


# ---- End of third party library code

def get_data_one(network):
    # Modify this function
    db = DataBase(network)
    result = ''
    try:
        result = db.read()
    except IOError as err:
        print(err)
    db.close()
    return result


def get_data_two(network):
    # Modify this function
    db = DataBase(network)
    result = ''
    try:
        result = db.read()
    finally:
        db.close()
    return result


class TestExceptions(unittest.TestCase):
    def test_raise_if_not_length_four(self):
        assert raise_if_not_length_four('ABCD') == 'ABCD'
        assert raise_if_not_length_four(['', '', '', '']) == ['', '', '', '']

    def test_raise_if_not_length_four_raises_ValueError(self):
        with pytest.raises(ValueError) as err:
            raise_if_not_length_four('')
        self.assertEqual(err.value.args[0], 'Argument must be length 4, not 0')

    def test_raise_if_not_four_characters(self):
        self.assertEqual(raise_if_not_four_characters('ABCD'), 'ABCD')

    def test_raise_if_not_four_characters_raises_ValueError(self):
        with pytest.raises(ValueError) as err:
            raise_if_not_four_characters('')
        self.assertEqual(err.value.args[0], 'Argument must be length 4, not 0')

    def test_raise_if_not_length_four_raises_TypeError(self):
        with pytest.raises(TypeError) as err:
            raise_if_not_four_characters(['', '', '', ''])
        self.assertEqual(err.value.args[0], "Argument must be a string, not <class 'list'>")

    def test_get_data_one_good_network(self):
        reset()
        assert get_data_one(GOOD_NETWORK) == 'Data...'
        assert DataBase.number_of_connections == 0

    def test_get_data_one_bad_network(self):
        reset()
        assert get_data_one(BAD_NETWORK) == ''
        assert DataBase.number_of_connections == 0

    def test_get_data_two_good_network(self):
        reset()
        assert get_data_two(GOOD_NETWORK) == 'Data...'
        assert DataBase.number_of_connections == 0

    def test_get_data_two_bad_network(self):
        reset()
        with pytest.raises(IOError) as err:
            get_data_two(BAD_NETWORK)
        assert err.value.args[0] == 'Ooops'
        assert DataBase.number_of_connections == 0
