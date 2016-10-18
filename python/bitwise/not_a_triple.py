import unittest


def not_a_triple(numbers):
    """
    Given an array where every element occurs three times, except one element.
    Find that element. Expected time complexity is O(n) and O(1) extra space.

    :param numbers:
    :return:
    """
    if len(numbers) % 3 == 0:
        raise Exception("Invalid input array")

    result = 0

    # Outer loop is constant so total runtime ~O(B*n) = O(n) where B is the sizeof(int)
    for bit_index in xrange(32):
        bit_sum = 0

        for n in numbers:
            bit_sum += (n & (1 << bit_index)) >> bit_index

        if bit_sum % 3 != 0:
            # The bit_sum of all the bits at this bit_index isn't a factor of 3
            # so the target number has a 1 at this bit position.
            result |= (1 << bit_index)

    return result


class TestNotATriple(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(not_a_triple([5, 5, 5, 3]), 3)
        self.assertEqual(not_a_triple([1, 4, 4, 4, 2, 2, 2]), 1)
        self.assertEqual(not_a_triple([10, 10, 8, 9, 2, 10, 9, 9, 8, 8]), 2)


if __name__ == "__main__":
    unittest.main()
