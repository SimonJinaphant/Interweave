def search_insert(numbers, target):
    """
    Given a sorted array and target value, return the index of the target in the array,
    if the target doesn't exist then return where it would be if it was in the array.

    :param numbers: List of integer numbers
    :param target: The value to find in the array
    :return: The index of target
    """
    lower_bound = 0
    upper_bound = len(numbers) - 1

    while lower_bound <= upper_bound:
        middle = lower_bound + (upper_bound - lower_bound)/2
        if numbers[middle] > target:
            upper_bound = middle - 1
        elif numbers[middle] < target:
            lower_bound = middle + 1
        else:
            return middle

    return lower_bound

assert search_insert([1,3,5,6], 5) == 2
assert search_insert([1,3,5,6], 2) == 1