import unittest


def flip_bit(bit):
    """
    Invert a bit regardless if its signed/unsigned
    :param bit: The bit to invert
    :return: The invert of the input bit
    """
    return 1 ^ bit


def max_bitwise(a, b):
    """Determine the maximum of two numbers without using if/else or comparision operators
    :param a: The number to compare
    :param b: The other number to compare
    :return: The largest of the two input
    """

    '''
    Max functions look at the sign of a - b;
    In binary the sign of a number (assuming 32-bit signed integer) is at bit index 31
    If that index is 0 the difference is positive and thus a >= b otherwise b > a
    '''
    difference = a - b
    difference_sign = (difference >> 31) & 1

    return a * flip_bit(difference_sign) + b * difference_sign


class MaxTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(max_bitwise(15, 9), max(15, 9))
        self.assertEqual(max_bitwise(9, 15), max(9, 15))
        self.assertEqual(max_bitwise(0, 5), max(0, 5))

    def test_negative(self):
        self.assertEqual(max_bitwise(0, -1), max(0, -1))
        self.assertEqual(max_bitwise(-1, 0), max(-1, 0))
        self.assertEqual(max_bitwise(-5, -12), max(-5, -12))
        self.assertEqual(max_bitwise(-12, -5), max(-12, -5))


if __name__ == "__main__":
    unittest.main()