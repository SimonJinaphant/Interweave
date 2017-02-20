def partition_difference(numbers):
    """
    Given a set of integers, divide it into two subsets such that the absolute difference
    between their sums is minimal.

    ie:
    Input:  arr[] = {1, 6, 11, 5}

    Output: 1
    Explanation:
    Subset1 = {1, 5, 6}, sum of Subset1 = 12
    Subset2 = {11}, sum of Subset2 = 11


    :param numbers: A set of integers
    :return: A tuple consisting of the two sets where the minimal is minimal and that minimal value
    """
    return _partition_difference2([], [], numbers, 0)


def _partition_difference2(left, right, numbers, i):

    if i == len(numbers):
        # Basecase: There's no more elements left in the original set
        return abs(sum(left) - sum(right)), left, right

    # Take the current leading number from the original set
    current = numbers[i]

    # Solve the sub-problems where we decide to either put that number in the left subset or the right subset
    new_left = left[:]
    new_left.append(current)

    new_right = right[:]
    new_right.append(current)

    return min(_partition_difference2(new_left, right[:], numbers, i+1),
               _partition_difference2(left[:], new_right, numbers, i+1))


print partition_difference([1,6,11,5])
