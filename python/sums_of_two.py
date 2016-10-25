def sums_of_two(numbers, target):
    """
    Given a sorted array of integers, find two values which add up to the target,
    and return their indices.

    :param numbers:
    :param target:
    :return:
    """

    lower = 0
    upper = len(numbers) - 1

    while lower <= upper:
        current_sum = numbers[lower]+numbers[upper]
        if current_sum > target:
            upper -= 1
        elif current_sum < target:
            lower += 1
        else:
            return lower, upper

    return None, None


def sums_of_two_unsorted(numbers, target):
    """
    Given an unsorted array of integers, find two values which add up to the target,
    and return their indices

    :param numbers:
    :param target:
    :return:
    """

    record = {}

    for i, num in enumerate(numbers):
        if num in record:
            return record[num], i
        else:
            record[target-num] = i

    return None, None

print sums_of_two([2, 7, 11, 15], 9)
print sums_of_two_unsorted([2, 7, 11, 15], 9)