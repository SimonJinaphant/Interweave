import unittest


def intersection(list_a, list_b):
    """
    Given two sorted list of numbers, determine the common numbers they share.

    :param list_a: The first list.
    :param list_b: The second list.
    :return: The common elements shared in both lists.
    """
    a = 0
    b = 0
    common = []

    while a < len(list_a) and b < len(list_b):
        if list_a[a] > list_b[b]:
            b += 1
        elif list_a[a] < list_b[b]:
            a += 1
        else:
            common.append(list_a[a])
            a += 1
            b += 1

    return common


class TestIntersection(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(intersection([1, 8, 10, 12, 14, 21, 22], [3, 10, 14, 15, 21]), [10, 14, 21])
        # No intersection
        self.assertEqual(intersection([1, 8, 10, 12, 22], [3, 14, 15, 21]), [])
        self.assertEqual(intersection([1, 8, 10, 12, 22], []), [])
        # All elements
        self.assertEqual(intersection([4, 10, 14, 19], [4, 10, 14, 19]), [4, 10, 14, 19])
        # Only first n
        self.assertEqual(intersection([4, 10, 14, 19, 21, 24, 50], [4, 10, 14, 19]), [4, 10, 14, 19])
        self.assertEqual(intersection([4, 10, 14, 19], [4, 10, 14, 19, 21, 42, 40]), [4, 10, 14, 19])


if __name__ == "__main__":
    unittest.main()