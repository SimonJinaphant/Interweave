import unittest

def multiply(a, b):
    """Multiply two positive integers
    :param a: First number
    :param b: Second number
    :return: The product of the two input numbers
    """

    bit_index = 0
    result = 0

    while b != 0:
        if b & 1 == 1:
            result += a << bit_index
        b >>= 1
        bit_index += 1

    return result

class MultiplyTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(multiply(10, 5), 10 * 5)
        self.assertEqual(multiply(4, 8), 4 * 8)


if __name__ == "__main__":
    unittest.main()