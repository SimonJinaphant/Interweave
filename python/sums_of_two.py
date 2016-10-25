import unittest


def sums_of_two(numbers, target):
    """
    Given a sorted array of integers, find two values which add up to the target,
    and return their indices.

    :param numbers: Array of integers in ascending order.
    :param target: The value to find in the array
    :return: A tuple of the indices for the two values which sums up to target, or (None, None)
    """

    lower = 0
    upper = len(numbers) - 1

    while lower < upper:
        current_sum = numbers[lower]+numbers[upper]

        if current_sum > target:
            # Take a smaller number since we've summed too much
            upper -= 1
        elif current_sum < target:
            # Take a larger number since we've summed to little
            lower += 1
        else:
            return lower, upper

    return None, None


def sums_of_two_unsorted(numbers, target):
    """
    Given an unsorted array of integers, find two values which add up to the target,
    and return their indices

    :param numbers: Array of integers that's unsorted
    :param target: The value to find in the array
    :return: A tuple of the indices for the two values which sums up to target, or (None, None)
    """
    # Key holds the number we need to find to sum to the target, value is the index of the first number
    record = {}

    for i, num in enumerate(numbers):
        if num in record:
            # We found a number we needed to reach the target
            return record[num], i
        else:
            # Record the number we want to find
            record[target-num] = i

    return None, None


class TestSumsOfTwo(unittest.TestCase):
    def test_sorted(self):
        self.assertEqual(sums_of_two([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(sums_of_two([2, 7, 11, 15], 17), (0, 3))
        self.assertEqual(sums_of_two([2, 7, 11, 15], 14), (None, None))

    def test_unsorted(self):
        self.assertEqual(sums_of_two_unsorted([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(sums_of_two_unsorted([2, 7, 11, 15], 17), (0, 3))
        self.assertEqual(sums_of_two_unsorted([2, 7, 11, 15], 14), (None, None))


if __name__ == "__main__":
    unittest.main()