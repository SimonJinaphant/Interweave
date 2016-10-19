def partition_search(input_numbers, key):
    """
    Search an unsorted array by partitioning sections of it.

    :param input_numbers: An array of numbers
    :param key: The value to find
    :return: Whether the array contains the key or not
    """
    lower_bound = 0
    upper_bound = len(input_numbers)-1

    # Copy the array to prevent mutation on original while partitioning
    numbers = input_numbers[:]

    while upper_bound >= lower_bound:
        pivot_index = three_way_partition(numbers, lower_bound, upper_bound)

        if numbers[pivot_index] > key:
            upper_bound = pivot_index - 1

        elif numbers[pivot_index] < key:
            lower_bound = pivot_index + 1

        else:
            return True

    return False


def three_way_partition(input_list, lower, upper):
    """
    Partition the array such that all elements < A[0] is to the left and all elements > A[0] are to the right.

    :param input_list: The array to mutate
    :param lower: Lower index to partition
    :param upper: Upper index to partition
    :return: The index of the first element with a value of A[0] (there could be duplicate keys)
    """
    lower_bound = lower
    upper_bound = upper

    pivot = input_list[lower_bound]

    i = lower

    while i <= upper_bound:
        current_number = input_list[i]
        if current_number < pivot:
            swap(input_list, i, lower_bound)
            i += 1
            lower_bound += 1

        elif current_number > pivot:
            swap(input_list, i, upper_bound)
            upper_bound -= 1

        else:
            i += 1

    return lower_bound


def swap(input_list, a, b):
    """
    Swaps two element inside a collection
    """
    temp = input_list[a]
    input_list[a] = input_list[b]
    input_list[b] = temp


x = [-32, 40, 2, 59, 40, -32, 50, -24, 9, -290]
for i in x:
    assert partition_search(x, i) == True

assert partition_search(x, 20) == False