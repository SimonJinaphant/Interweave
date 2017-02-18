def max_sum_non_adj(numbers):
    """
    Given an array of positive numbers find the max sum subsequence such that
    elements in this subsequence ar enot adjacent to each other.

    :param numbers: Array of positive integer numbers
    :return: Maximum sum of sub-sequence which are not adjacent to each other
    """

    """
    Consider recording two pieces of data as we traverse the array: inclusive and exclusive

    @inclusive states the max sum we've obtained by including the current number and all non-adjacent number before it
    @exclusive states the max sum we've obtained by excluding the current number

    When we reach a new number we check if we should include the number or not by comparing the max
    of the current inclusive to the exclusive + that number
    """
    inclusive = numbers[0]
    exclusive = 0

    for i in xrange(1, len(numbers)):
        # Remember the old inclusive as it will become the new exclusive should we find a higher max
        temp = inclusive

        inclusive = max(exclusive+numbers[i], inclusive)
        exclusive = temp

    return inclusive


print max_sum_non_adj([4, 1, 1, 4, 2, 1])