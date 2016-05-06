import unittest

def next_ones(bin):
    i = 0
    msb = 0
    ones_count = 0

    while bin > 0:
        if bin & 1 == 1:
            ones_count += 1

        if bin == 1:
            msb = i

        i += 1
        bin >>= 1

    lower_ones = (1 << ones_count) - 1
    upper_ones = ((1 << msb+1) - 1) & ~((1 << msb - ones_count + 1) - 1)

    return upper_ones, lower_ones


class TestNextOnes(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(next_ones(0b1101), (0b1110, 0b0111))
        self.assertEqual(next_ones(0b1001), (0b1100, 0b0011))

    def test_bounds(self):
        self.assertEqual(next_ones(0b0), (0b0, 0b0))
        self.assertEqual(next_ones(0b1), (0b1, 0b1))
        self.assertEqual(next_ones(0b1111), (0b1111, 0b1111))


if __name__ == "__main__":
    unittest.main()