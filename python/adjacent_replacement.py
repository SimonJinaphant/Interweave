import unittest


def adjacent_replacement(number):
    """
    You are given an integer X. You must choose two adjacent digits and replace them with the larger of these two digits

    For example, from the integer X = 233614, you can obtain:
    33614 (by replacing 23 with 3);
    23614 (by replacing 33 with 3 or 36 with 6);
    23364 (by replacing 61 with 6 or 14 with 4);

    You want to find the smallest number that can be obtained from X by replacing two adjacent digits with the larger
    of the two. In the above example, the smallest such number is 23364.

    :param number: The number to perform replacement on
    :return: The smallest number from adjacent replacing digits
    """
    original = number
    max_digit = -1
    max_digit_index = -1
    digit_index = 0

    while number > 0:
        current_digit = number % 10
        if current_digit > max_digit or (current_digit == max_digit and max_digit_index == digit_index+1):
            max_digit = current_digit
            max_digit_index = digit_index
        digit_index += 1
        number /= 10

    assert max_digit_index >= 0

    if max_digit_index == 0:
        return (original / pow(10, max_digit_index+2)) * pow(10, max_digit_index+1) + max_digit

    else:
        leading_numbers = (original / pow(10, max_digit_index+1)) * pow(10, max_digit_index)
        trailing_numbers = original % pow(10, max_digit_index-1)

        return leading_numbers + max_digit * pow(10, max_digit_index-1) + trailing_numbers


class AdjacentReplacementTest(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(adjacent_replacement(233614), 23364)
        self.assertEqual(adjacent_replacement(10), 1)
        self.assertEqual(adjacent_replacement(153), 15)
        self.assertEqual(adjacent_replacement(159), 19)
        self.assertEqual(adjacent_replacement(3159), 319)
        self.assertEqual(adjacent_replacement(9513), 913)
        self.assertEqual(adjacent_replacement(91593), 9159)
        self.assertEqual(adjacent_replacement(19321), 1921)
        self.assertEqual(adjacent_replacement(9159), 919)
        self.assertEqual(adjacent_replacement(129159), 12919)