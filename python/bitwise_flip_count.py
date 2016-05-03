import unittest

def numberOfFlips(a, b):
    counter = 0;

    while a > 0 or b > 0:
        if (a & 1) ^ (b & 1) == 1:
            counter += 1
        a >>= 1
        b >>= 1

    return counter

class TestNumberOfFlips(unittest.TestCase):
    def test_normals(self):
        self.assertEqual(numberOfFlips(0b11101, 0b01111), 2)
        self.assertEqual(numberOfFlips(0b0, 0b0), 0)
        self.assertEqual(numberOfFlips(0b11111, 0b11111), 0)
        self.assertEqual(numberOfFlips(0b11111, 0b00000), 5)

if __name__ == "__main__":
    unittest.main()