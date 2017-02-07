def counting_bits(num):
    """
    For every numbers i in the range 0 <= i <= num calculate the number of 1's in their binary
    representation and return them as an array.

    Example:
    For num = 5 you should return [0,1,1,2,1,2].

    :param num: A non-negative integer
    :return: List of numbers of 1's for every number leading upto num (inclusive).
    """

    # Create a list of num+1 elements (we're including 0)
    result = [0] * (num+1)

    for i in xrange(1, num+1):
        """
        Mind-blown approach:

        Given a number N, if N is odd, it has a 1 in its binary LSB.
        The remaining amount of 1's can be determine by solving the sub-problem of the binary without the LSB,
        which is the same as right shifting N by 1 (or dividing by 2)

        Let F(n) determine the number of 1's in n's binary representation:
        F(n) = F(n >> 1) + (1 if n is odd, else 0)
             = F(n >> 1) + (n & 1)
        """
        result[i] = result[i >> 1] + (i & 1)

    return result

print counting_bits(5)
print counting_bits(10)
print counting_bits(15)