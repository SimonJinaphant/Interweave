def pair_swap(a):
    """
    Swap odd-even pairs of adjacent bits
    :param a: The binary input in the form A_n, ...A3, A2 A1, A0
    :return: Binary of the form A_n-1, A_n, ... A2, A3, A0, A1
    """
    swapped = 0

    while a > 0:
        print bin(swapped)
        if (a & 0b11 == 1) or (a & 0b11 == 2):
            swapped |= ((a & 0b11) ^ 0b11)
        else:
            swapped |= (a & 0b11)
        print bin(a & 0b11), "-"
        print bin(swapped)

        swapped <<= 2
        a >>= 2

        print bin(swapped)

    return swapped

print bin(pair_swap(0b001101))