import unittest

"""Some exercises involving lists.

creating lists
==============
a='A'
b='B'
c='C'
x = list()
add a, b, c into x
print the length of x

selecting from lists
====================
Given the list
x = ['A', 'B', 'C']
return the first item
return the last item
return the x reversed using indexing

selecting first items
======================= 
Given the following:
x = [('A','x'), ('B','y'), ('C','z')]
return ['A','B','C']

add 5 to values
=================
Given the following:
x = [1, 10, 20]
return a list with 5 added to the numbers i.e. [6, 15, 25]

divisible by 5
==================
Given the following:
x = [1, 10,  15, 3, 12, 15, 25, 50]
return a list with only numbers divisible by 5 (% modulo operator)

merge_lists
===================
given the lists:
x = ['A', 'B', 'C']
y = ['x', 'y', 'z']
create the following list:
[('A','x'), ('B','y'), ('C','z')]

transpose()
===========
Create a function that takes a list of lists and returns the transpose. So given:
[
    [1, 2, 3],
    ['A', 'B', 'C'],
]

We would expect:
[
    [1, 'A'],
    [2, 'B'],
    [3, 'C'],
]

In the case of uneven length lists choose then truncate to the shortest, so given:
[
    [1, 2, 3],
    ['A', 'B'],
]

We would expect:
[
    [1, 'A'],
    [2, 'B'],
]

Hint: There is a builtin function that can help you.

peak_to_peak()
==============
Create a function that returns the peak-to-peak value of the values in a list.

Hint: There are a couple of builtin functions that can help you.

Challenges: What to do when the list is empty?
If the list contains non-numeric values?

list rotation
=============
Rotate a list by taking the value from one end a putting it on the other end.
Create two functions rotate_left() and rotate_right() that modify a list in
place as follows, given the list ['A', 'B', 'C']:

rotate_left() changes it to ['B', 'C', 'A']
rotate_right() changes it to ['C', 'A', 'B']

More: The solution has two failing tests, fix the solution so that the tests pass.

Created on 21 Feb 2016

@author: paulross
"""


def create_list():
    """Create a list."""
    a = 'A'
    b = 'B'
    c = 'C'
    return [a, b, c]


def select_first_item():
    """Return first item."""
    x = ['A', 'B', 'C']
    return x[0]


def select_last_item():
    """Return last item."""
    x = ['A', 'B', 'C']
    return x[-1]


def select_reversed():
    """Return list reversed."""
    x = ['A', 'B', 'C']
    return x[::-1]


def select_first_items():
    """Select first item on each list."""
    x = [('A', 'x'), ('B', 'y'), ('C', 'z')]
    return [a for a, b in x]


def add_5_to_values():
    """Return the list with 5 added to each value."""
    x = [1, 10, 20]
    return [a + 5 for a in x]


def get_divisble_by_5():
    """Return elements that are divisble by 5."""
    x = [1, 10, 15, 3, 12, 15, 25, 50]
    return list(filter(lambda x: not x % 5, x))


def merge_lists():
    """Returns pairs from each list."""
    x = ['A', 'B', 'C']
    y = ['x', 'y', 'z']
    return list(zip(x, y))


def transpose(list_of_lists):
    """Transpose a list of lists."""
    # Your code goes here
    return [list(v) for v in zip(*list_of_lists)]


def peak_to_peak(alist):
    """Return the peak to peak value of a list."""
    return max(alist) - min(alist)


def rotate_left(alist):
    """Rotates a list to the left so that the first item appears at the end."""
    if len(alist):
        alist.append(alist.pop(0))


def rotate_right(alist):
    """Rotates a list to the right so that the last item appears at the beginning."""
    if len(alist):
        alist.insert(0, alist.pop())


class TestListsTuples(unittest.TestCase):
    def test_create_list(self):
        assert create_list() == ['A', 'B', 'C']

    def test_select_first_item(self):
        assert select_first_item() == 'A'

    def test_select_last_item(self):
        assert select_last_item() == 'C'

    def test_select_reversed(self):
        assert select_reversed() == ['C', 'B', 'A']

    def test_select_first_items(self):
        assert select_first_items() == ['A', 'B', 'C']

    def test_add_5_to_values(self):
        assert add_5_to_values() == [6, 15, 25]

    def test_get_divisble_by_5(self):
        assert get_divisble_by_5() == [10, 15, 15, 25, 50]

    def test_merge_lists(self):
        assert merge_lists() == [('A', 'x'), ('B', 'y'), ('C', 'z')]

    def test_transpose(self):
        data = [
            [1, 2, 3],
            ['A', 'B', 'C'],
        ]
        expected = [
            [1, 'A'],
            [2, 'B'],
            [3, 'C'],
        ]
        assert transpose(data) == expected

    def test_transpose_non_equal_length(self):
        data = [
            [1, 2, 3],
            ['A', 'B'],
        ]
        expected = [
            [1, 'A'],
            [2, 'B'],
        ]
        assert transpose(data) == expected

    def test_peak_to_peak(self):
        assert peak_to_peak([1, 8]) == 7
        assert peak_to_peak([-1, -8]) == 7
        assert peak_to_peak([9, -8]) == 17

    def test_rotate_left(self):
        l = ['A', 'B', 'C']
        rotate_left(l)
        assert l == ['B', 'C', 'A']

    def test_rotate_right(self):
        l = ['A', 'B', 'C']
        rotate_right(l)
        assert l == ['C', 'A', 'B']

    def test_rotate_left_empty(self):
        l = []
        rotate_left(l)
        assert l == []

    def test_rotate_right_empty(self):
        l = []
        rotate_right(l)
        assert l == []
