import unittest

def pair_swap(a):
    """
    Swap odd-even pairs of adjacent bits
    :param a: The binary input in the form A_n, ...A3, A2 A1, A0
    :return: Binary of the form A_n-1, A_n, ... A2, A3, A0, A1
    """
    swapped = 0
    index = 0

    while a > 0:

        if (a & 0b11 == 1) or (a & 0b11 == 2):
            swapped |= (((a & 0b11) ^ 0b11) << index)
        else:
            swapped |= ((a & 0b11) << index)

        index += 2
        a >>= 2

    return swapped


class TestPairSwap(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(pair_swap(0b1101), 0b1110)
        self.assertEqual(pair_swap(0b0), 0b0)
        self.assertEqual(pair_swap(0b1000), 0b0100)
        self.assertEqual(pair_swap(0b1000 - 1), 0b1011)

if __name__ == "__main__":
    unittest.main()