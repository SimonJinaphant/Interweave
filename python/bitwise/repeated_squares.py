import unittest


def exponential(base, expo):
    """
    Calculate the power given an integer base and a positive integer expo
    :param base: Base number
    :param expo: Exponent number
    :return: base raised to the expo power
    """
    result = 1
    current_base = base

    while expo != 0:
        if expo & 1:
            result *= current_base

        current_base *= current_base

        expo >>= 1

    return result


class ExponentialTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(exponential(10, 5), 10**5)
        self.assertEqual(exponential(10, 2), 10**2)
        self.assertEqual(exponential(5, 5), 5**5)

    def test_edge(self):
        self.assertEqual(exponential(3,0), 3**0)
        self.assertEqual(exponential(3,1), 3**1)

    def test_neg(self):
        self.assertEqual(exponential(-3,2), (-3)**2)
        self.assertEqual(exponential(-3,3), (-3)**3)


if __name__ == "__main__":
    unittest.main()