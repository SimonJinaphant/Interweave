from math import floor, ceil


def integer_break(number):
    """
    Given a positive integer n, decompose it into the sum of at least two positive integers and
    maximize the product of those integers.

    Given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

    :param number: 2 <= number < 58
    :return: The maximum product of all its sum fragments
    """

    fragments = [number]
    result = 1

    while len(fragments) != 0:
        current = fragments.pop()

        lower_fragment = int(floor(current/2.0))
        upper_fragment = int(ceil(current/2.0))

        if lower_fragment <= 3:
            result *= lower_fragment
        else:
            fragments.append(lower_fragment)

        if upper_fragment <= 3:
            result *= upper_fragment
        else:
            fragments.append(upper_fragment)

    return result

print integer_break(5)
print integer_break(10)