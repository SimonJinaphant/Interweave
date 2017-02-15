import unittest


def sums_of_three_to_target(numbers, target):
    """
    Given an unsorted array of numbers, find if three of its elements can sum to zero

    :param numbers: An array of unsorted integers that has a minimum of 3 elements
    :return: True if there exist 3 elements which sums to 0
    """

    for i in xrange(0, len(numbers)-2):
        # Per each iteration we have 1 of 3 numbers to possibly sum to @target

        # To remember what number we want to find later on
        record = set([])

        for j in xrange(i+1,len(numbers)):
            # Per each iteration we have 2 of 3 numbers to possible sum to @target

            if numbers[j] not in record:
                # The current 2nd number wasn't a number we were looking for, so we'll remember it
                record.add(target-(numbers[i]+numbers[j]))
            else:
                # We found that number we wanted to
                return True

    return False


class SumsOfThreeTest(unittest.TestCase):
    def test_to_zero(self):
        self.assertEqual(sums_of_three_to_target([-5, 0, -2, 3, 120], 0), False)
        self.assertEqual(sums_of_three_to_target([-5, 0, -2, 7, 120], 0), True)
        self.assertEqual(sums_of_three_to_target([-1, 1, 0], 0), True)
        self.assertEqual(sums_of_three_to_target([-1, 2, 0], 0), False)
        self.assertEqual(sums_of_three_to_target([-100, -80, -50, -70, 150], 0), True)

    def test_to_targets(self):
        self.assertEqual(sums_of_three_to_target([-5, 0, -2, 3, 120], -4), True)
        self.assertEqual(sums_of_three_to_target([-1, 1, 0], 1), False)
        self.assertEqual(sums_of_three_to_target([-100, -80, -50, -70, 150], -30), True)

if __name__ == "__main__":
    unittest.main()