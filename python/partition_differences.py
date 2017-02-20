def partition_difference2(left, right, numbers, i):
    """
    Given a set of integers, divide it into two subsets such that the absolute difference
    between their sums is minimal.

    ie:
    Input:  arr[] = {1, 6, 11, 5}

    Output: 1
    Explanation:
    Subset1 = {1, 5, 6}, sum of Subset1 = 12
    Subset2 = {11}, sum of Subset2 = 11

    :param left: The left subset
    :param right: The right subset
    :param numbers: The original set of numbers
    :param i: The current number we're looking at in @numbers
    """

    if i == len(numbers):
        # Basecase: There's no more elements left in the original set
        return [abs(sum(left) - sum(right)), left, right]

    # Take the current leading number from the original set
    current = numbers[i]

    # Solve the sub-problems where we decide to either put that number in the left subset or the right subset
    new_left = left[:]
    new_left.append(current)

    new_right = right[:]
    new_right.append(current)

    return min(partition_difference2(new_left, right[:], numbers, i+1),
               partition_difference2(left[:], new_right, numbers, i+1))


print partition_difference2([], [], [1,6,11,5], 0)


