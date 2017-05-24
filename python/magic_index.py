from __future__ import absolute_import
import unittest


def magic_index(numbers):
    """A magic index of an array is one where A[i] == i.
    Determine the magic index of an array, if one exist

    :param numbers: A increasing distinct list of integers
    :return: The first magic index, if one exist
    """

    """
    Since the array is sorted we can use this to our advantage.

    If we take any arbitrary index i in the array we can determine if the magic index is in the left or right sub-array
    If i > A[i] then any elements to the left cannot be a magic index because they will be smaller than their own index.
    If i < A[i] then any elements to the right cannot be a magic index because it will be larger than their own index.
    If i == A[i] then we found our answer!

    So we'll try a binary-search like approach by starting in the middle, and adjust the upper and lower bounds of the
    search based on the comparision of i and A[i].
    """

    lower_bound = 0
    upper_bound = len(numbers) -1

    while lower_bound <= upper_bound:
        mid = lower_bound + ((upper_bound - lower_bound) / 2)

        if numbers[mid] == mid:
            return mid
        elif numbers[mid] > mid:
            # All elements to the right will be larger than their own index so we need to search the left sub-array.
            upper_bound = mid - 1
        else:
            # All elements to the left will be smaller than their own index so we need to search the right sub-array.
            lower_bound = mid + 1

    return None


class TestMagicIndex(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(magic_index([-40, -20, -1, 1, 2, 3, 5, 6, 7, 9, 12, 13]), 9)
        self.assertEqual(magic_index([-40, -20, 1, 3, 5, 6, 7, 9, 13]), 3)

    def test_none(self):
        self.assertEqual(magic_index([1, 2, 3]), None)
        self.assertEqual(magic_index([1]), None)

if __name__ == "__main__":
    unittest.main()
