def get_bit(binary, bit_index):
    return (binary & (1 << bit_index)) >> bit_index


def missing_binary(bin_sequence):
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
        #There's more 0 bits, indicating that the missing binary is odd
        #so we'll search all odd binaries
        return (_missing_binary(lsb_of_ones, current_index+1) << 1) | 1