import unittest


def equilibrium_array(numbers):
    """Determine the equilibrium index of the given numbers

    :param numbers: The collection of integer numbers (non-null) to test on
    :return: An integer P such that 0 <= P < N and the sum of elements of lower
    indices is equal to the sum of elements of higher indices.

    If no index is found: None is returned
    """
    left = [None] * len(numbers)
    right = [None] * len(numbers)

    left[0] = 0
    right[-1] = 0

    size = len(numbers)
    for i in xrange(1, size):
        left[i] = numbers[i-1] + left[i-1]
        right[size-i-1] = numbers[size-i] + right[size-i]

    for k in xrange(0, size):
        if left[k] == right[k]:
            return k

    return None


class TestEquilibriumArray(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(equilibrium_array([-7, 1, 5, 2, -4, 3, 0]), 3)
        self.assertEqual(equilibrium_array([1, 2, 3, 4, 5, 4, 3, 2, 1]), 4)

    def test_ends(self):
        self.assertEqual(equilibrium_array([99, 0, 66, 32, 1]), 1)
        self.assertEqual(equilibrium_array([1, 32, 66, 0, 99]), 3)

        self.assertEqual(equilibrium_array([0, -99, 66, 32, 1]), 0)
        self.assertEqual(equilibrium_array([1, 32, 66, 0, -99]), None)

    def test_single(self):
        self.assertEqual(equilibrium_array([0]), 0)

if __name__ == "__main__":
    unittest.main()
