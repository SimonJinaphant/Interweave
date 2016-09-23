import unittest


def sums_of_three(numbers):
    """
    Given an array of numbers, find if three of its elements can sum to zero

    :param numbers: An array of unsorted integers that has a minimum of 3 elements
    :return: True if there exist 3 elements which sums to 0
    """

    for i in xrange(len(numbers)-2):

        # record is a set of numbers we need to get one sum of zero
        record = set([])

        for j in xrange(i+1, len(numbers)):
            if numbers[j] not in record:
                # Calculate the number we need to find to sum to 0
                record.add(-(numbers[i]+numbers[j]))
            else:
                return True

    return False


class SumsOfThreeTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(sums_of_three([-5, 0, -2, 3, 120]), False)
        self.assertEqual(sums_of_three([-5, 0, -2, 7, 120]), True)
        self.assertEqual(sums_of_three([-1, 1, 0]), True)
        self.assertEqual(sums_of_three([-1, 2, 0]), False)
        self.assertEqual(sums_of_three([-100, -80, -50, -70, 150]), True)

if __name__ == "__main__":
    unittest.main()