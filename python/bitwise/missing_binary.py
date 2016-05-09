import unittest


def get_bit(binary, bit_index):
    """Retrieve the bit at the specified index of a given binary number

    :param binary: The binary number,
    :param bit_index: The index to look at; 0 <= index < binary.length
    :return: The specific bit, 0 or 1, corresponding to the bit_index of binary
    """
    return (binary & (1 << bit_index)) >> bit_index


def missing_binary(bin_sequence):
    """Given an ordered list of binary numbers whose values range from 0 to N (inclusive), there is
    an element that is missing, find that value within linear time.

    :param bin_sequence: An ordered sequence of integers from 0 to N (inclusive) with one missing number
    :return: The missing number n of the sequence. 0 <= n < N
    """
    return _missing_binary(bin_sequence, 0)


def _missing_binary(bin_sequence, current_index):
    if current_index >= 32:
        return 0

    lsb_of_ones = []
    lsb_of_zeros = []

    for bin in bin_sequence:
        if get_bit(bin, current_index) == 0b1:
            lsb_of_ones.append(bin)
        else:
            lsb_of_zeros.append(bin)

    if len(lsb_of_zeros) <= len(lsb_of_ones):
        return (_missing_binary(lsb_of_zeros, current_index+1) << 1) | 0
    else:
        #There's more 0 bits, indicating that the missing binary has LSB of 1
        #so we'll continue the search with all binaries with LSB of 1
        return (_missing_binary(lsb_of_ones, current_index+1) << 1) | 1


class TestMissingBinary(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(missing_binary([0, 1, 2, 4]), 0b11)
        self.assertEqual(missing_binary([1, 2, 3]), 0)


if __name__ == "__main__":
    unittest.main()