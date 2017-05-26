from __future__ import absolute_import
import unittest


def subarray_sum_to_target(numbers, target):
    """
    Determine the contiguous sub-array whose elements all sum to the target number

    :param numbers: Unsorted array of positive integer numbers
    :param target: The target value of the sub-array's sum

    :return: The subarray whose element all sum to the target
    """

    """
    Create a sub-array define by the lower and upper bounds starting at indices 0 and 1
    Depending on the sub-array's sum compared to the target sum, we'll expand the array by including the next number
    or shrink the sub-array by excluding the leftmost number.
    """
    start = 0
    end = 1
    current_sum = numbers[start]

    while end < len(numbers):
        if current_sum < target:
            # The target is still larger than our sub-array's sum, expand the upper bound by one
            current_sum += numbers[end]
            end += 1
        elif current_sum > target:
            # The target is smaller than our sub-array's sum, shrink the sub-array by removing the leftmost element
            current_sum -= numbers[start]
            start += 1
        else:
            break

    return numbers[start: end]


class SubarraySumToTargetTest(unittest.TestCase):

    def test_valid(self):
        self.assertEquals(subarray_sum_to_target([1, 4, 20, 3, 10, 5], 33), [20, 3, 10])
        self.assertEquals(subarray_sum_to_target([1, 4, 0, 0, 3, 10, 5], 7), [4, 0, 0, 3])
        self.assertEqual(subarray_sum_to_target([1, 3, 10, 5, 1, 6], 16), [10, 5, 1])

    def test_invalid(self):
        self.assertEquals(subarray_sum_to_target([1, 4], 0), [])

if __name__ == "__main__":
    unittest.main()