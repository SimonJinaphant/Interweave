def single_numbers(numbers):
    """
    Given a array of numbers, where exactly two numbers appear only once (a, b)
    and all other elements appear twice, find a and b.

    :param numbers: Array of positive non-zero number which contains a duplicate for all elements except two.
    :return: The two exceptional numbers which didn't appear twice.
    """
    xor_result = 0
    for num in numbers:
        xor_result ^= num

    # We're interested in a bit position with value 1 of the xor_result
    # it tells which bit to compare all other number against to find either a or b
    interesting_bit = 1
    while xor_result & interesting_bit == 0:
        interesting_bit <<= 1

    first_single = 0
    second_single = 0
    for num in numbers:
        if num & interesting_bit == 0:
            first_single ^= num
        else:
            second_single ^= num

    return first_single, second_single


print single_numbers([1,2,1,3,2,5])