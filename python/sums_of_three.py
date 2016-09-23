def sums_of_three(numbers):
    """
    Given an array of numbers, find if three of its elements can sum to zero

    :param numbers: An array of unsorted integers
    :return: True if there exist 3 elements which sums to 0
    """

    for i in xrange(len(numbers)-2):

        # record is a set of numbers we need to get one sum of zero
        record = set([])

        for j in xrange(i+1, len(numbers)):
            if numbers[j] not in record:
                # Calculate the number we need to find to sum to 0
                record.add(-(numbers[i]+numbers[j]))
            else:
                return True

    return False

print sums_of_three([-5, 0, -2, 3, 120])