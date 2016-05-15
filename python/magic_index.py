import unittest


def magic_index(numbers):
    """A magic index of an array is one where A[i] == i.
    Determine the magic index of an array, if one exist

    :param numbers: A increasing distinct list of integers
    :return: The first magic index, if one exist
    """
    lower_bound = 0
    upper_bound = len(numbers) -1

    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound) / 2

        if numbers[mid] == mid:
            return mid
        elif numbers[mid] > mid:
            upper_bound = mid - 1
        else:
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
