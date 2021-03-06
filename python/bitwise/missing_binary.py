import unittest


def get_bit(binary, bit_index):
    """Retrieve the bit at the specified index of a given binary number

    :param binary: The binary number,
    :param bit_index: The index to look at; 0 <= index < binary.length
    :return: The specific bit, 0 or 1, corresponding to the bit_index of binary
    """
    return (binary & (1 << bit_index)) >> bit_index


def missing_binary(bin_sequence):
    """Given an unsorted list of N unique 32-bit binary sequences whose decimal values ranges from 0 to N (inclusive),
    there is one binary sequence that is missing, find that value.

    Note: Unlike an array of normal integers ie: [0, 1, 2, 4] you are not allowed to perform mathematical operators
    such as + - * / on these binary sequences. Therefore you cannot simply sum up the list and subtract it
    from the expected sum to determine the missing number.

    :param bin_sequence: An list of unique integers from 0 to N (inclusive) with one missing number
    :return: The missing number n of the sequence. 0 <= n < N
    """
    return _missing_binary(bin_sequence, 0)


def _missing_binary(bin_sequence, current_index):

    # Basecase: Reached maximum amount of bit possible
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
        # There's more 1 bits, indicating that the missing binary has bit value of 0 at the current bit index
        # We'll continue the search with the smaller subset of binary sequences

        return (_missing_binary(lsb_of_zeros, current_index+1) << 1) | 0

    else:
        # There's more 0 bits, indicating that the missing binary has bit value of 1 at the current bit index
        # We'll continue the search with this smaller subset of binary sequences

        # (n << 1) | 1  is a shorthand for appending a bit in the LSB position with the value 1
        # ex: If n = 0100 then the above will create 010001
        return (_missing_binary(lsb_of_ones, current_index+1) << 1) | 1


class TestMissingBinary(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(missing_binary([0, 1, 2, 4]), 0b11)
        self.assertEqual(missing_binary([2, 1, 3]), 0)
        self.assertEqual(missing_binary([3, 4, 2, 0]), 0b1)
        self.assertEqual(missing_binary([0, 0, 1, 2, 4]), 0b11)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(missing_binary([0,1,3,4], 0b1))
        self.assertEqual(missing_binary([0,1,2,3]), 0b100)

if __name__ == "__main__":
    unittest.main()