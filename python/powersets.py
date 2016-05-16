import unittest
from copy import deepcopy


def powersets(elements, current=0):
    """Generate a set of all subset

    :param elements: A set of elements
    :param current: The current index to permute on
    :return: A set containing all subsets of the input set
    """
    if len(elements) == current:
        return [[]]

    #A powerset P(n) is composed of P(n-1) unioned with (P(n-1) + n)

    subset_previous = powersets(elements, current + 1)
    subset_current = deepcopy(subset_previous)

    for sub in subset_current:
        sub.append(elements[current])

    #Using extends() seems to cause unexpected behavior with nested lists
    new_subset = subset_previous
    for sub in subset_current:
        new_subset.append(sub)

    return new_subset


class TestPowerSets(unittest.TestCase):

    """
    Due to python's set being unhashable, nested sets are not possible
    A list is used instead, so order will matter in testcases.
    """

    def test_normals(self):
        self.assertEqual(powersets([]), [[]])
        self.assertEqual(powersets([1]), [[],[1]])
        self.assertEqual(powersets([1,2]), [[], [2], [1], [2, 1]])


if __name__ == "__main__":
    unittest.main()