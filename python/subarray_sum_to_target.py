from __future__ import absolute_import
import unittest


def subarray_sum_to_target(numbers, target):
    start = 0
    end = 1
    current_sum = numbers[start]

    while end != len(numbers):
        if current_sum < target:
            current_sum += numbers[end]
            end += 1
        elif current_sum > target:
            current_sum -= numbers[start]
            start += 1
        else:
            return numbers[start: end]

    return None


class SubarraySumToTargetTest(unittest.TestCase):

    def test_valid(self):
        self.assertEquals(subarray_sum_to_target([1, 4, 20, 3, 10, 5], 33), [20, 3, 10])
        self.assertEquals(subarray_sum_to_target([1, 4, 0, 0, 3, 10, 5], 7), [4, 0, 0, 3])
        self.assertEqual(subarray_sum_to_target([1, 3, 10, 5, 1, 6], 16), [10, 5, 1])

    def test_invalid(self):
        self.assertEquals(subarray_sum_to_target([1, 4], 0), [])

if __name__ == "__main__":
    unittest.main()