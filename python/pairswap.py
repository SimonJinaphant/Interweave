def pair_swap(a):
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