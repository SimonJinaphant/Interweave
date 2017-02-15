def _interleave_print(left, right, current):
    if len(left) == 0 and len(right) == 0:
        print current
        return

    if len(left) != 0:
        _interleave_print(left[1:], right[:], current[:]+left[0])

    if len(right) != 0:
        _interleave_print(left[:], right[1:], current[:]+right[0])


def interleave_print(left, right):
    _interleave_print(left, right, "")

interleave_print("ab", "cd")