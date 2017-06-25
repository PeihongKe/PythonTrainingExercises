import random
import unittest


def what_sign(n):
    """
    Write a function 'what_sign' which returns 'Positive' 'Zero' or 'Negative' when given a number
    """
    return 'Positive' if n > 0 else 'Negative' if n < 0 else 'Zero'


def fizzbuzz():
    """
    Write a program that prints the integers from 1 to 100.

    But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
    For numbers which are multiples of both three and five print "FizzBuzz".
    """
    return '\n'.join(['Fizz' * (x % 3 == 0) + 'Buzz' * (x % 5 == 0) or str(x) for x in range(1, 101)])


def remove_indices(mylist, idxs):
    """
    Write a function which removes one or more indicies from a list.

    For example given the list:
    ["John", "Bob", "Charles", "Trev"]
    and the indices:
    [1, 2]
    the resulting list will be:
    ["John", "Trev"]
    """
    result = []
    for i, v in enumerate(mylist):
        if i not in idxs:
            result.append(v)
    return result


def open_connection():
    if random.randint(0, 3) != 0:
        raise ValueError('failed to connect')
    return True


def connect(retry=100):
    """"
    Modify connect to handle failed connections

    Your code to handle bad connection goes here
    You might need to modify the arguments passed to connect() such as
    how many times the caller wants to try to make a connection before
    giving up.
    """
    for _ in range(retry + 1):
        try:
            return open_connection()
        except ValueError:
            pass
    return False


class TestControlFlow(unittest.TestCase):
    def test_fizz_buzz(self):
        assert fizzbuzz()

    def test_what_sign(self):
        self.assertEqual(what_sign(3), 'Positive', )
        self.assertEqual(what_sign(0), 'Zero', )
        self.assertEqual(what_sign(-3), 'Negative', )

    def test_remove_indices(self):
        self.assertEqual(remove_indices(["John", "Bob", "Charles", "Trev"], [0]), ["Bob", "Charles", "Trev"])
        self.assertEqual(remove_indices(["John", "Bob", "Charles", "Trev"], [1, 2]), ["John", "Trev"])

    def test_connect(self):
        for _i in range(100):
            assert connect()
