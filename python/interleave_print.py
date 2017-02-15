def _interleave_print(left, right, current):
    """
    Given two strings, print all interleaved strings where the order of the letters are preserved

    :param left: One of the strings to choose characters from
    :param right: Another string to choose characters from
    :param current: The current string composed so far
    """

    # We are done when we have no more character to take from either strings
    if len(left) == 0 and len(right) == 0:
        print current
        return

    if len(left) != 0:
        # Take the leading left character as the next character in our interleaved string
        _interleave_print(left[1:], right[:], current[:]+left[0])

    if len(right) != 0:
        # Take the leading right character as the next character in our interleaved string
        _interleave_print(left[:], right[1:], current[:]+right[0])


def interleave_print(left, right):
    """
    Given two strings, print all interleaved strings.

    An interleaved string of given two strings preserves the order of characters in individual strings.
    For example, in all the interleavings of "ABCD" first example, A comes before B and C comes before D.

    :param left: One of the two strings
    :param right: Another one of the two strings
    """
    _interleave_print(left, right, "")

interleave_print("ab", "cd")