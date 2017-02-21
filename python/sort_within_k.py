import heapq


def swap(numbers, i, j):
    temp = numbers[i]   # 3
    numbers[i] = numbers[j]
    numbers[j] = temp


def sort_within_k(numbers, k):
    """
    Given an array arr of length n where each element is at most k places away from its sorted position, sort the array

    Example: n=10, k=2. The element belonging to index 6 in the sorted array, may be at indices 4, 5, 6, 7 or 8

    :param numbers: Array of integers
    :param k: Positive integer denoting how far off from the correct spot a number is
    :return:
    """
    for i in xrange(len(numbers) - 1):
        min_index = i
        for j in xrange(i+1, min(i+k, len(numbers) - 1)+1):
            if numbers[j] < numbers[min_index]:
                min_index = j

        swap(numbers, i, min_index)

    return numbers


def sort_within_k_optimized(numbers, k):
    # Mapping for value to index, only needed for sorting array in place via swapping
    # We can't easily put the index in the heap element as well since we'll need to update it
    value_to_index = {}

    # Construct a min_heap for the first k-1 elements and remember their indices
    min_heap = []
    for i, element in enumerate(numbers[:k]):
        value_to_index[element] = i
        min_heap.append(element)
    heapq.heapify(min_heap)

    for i in xrange(len(numbers)-1):
        # Add the far element K can reach
        next_k_index = min(i+k, len(numbers)-1)
        heapq.heappush(min_heap, numbers[next_k_index])
        value_to_index[numbers[next_k_index]] = next_k_index

        # Find what is the current min element and its index
        min_element = heapq.heappop(min_heap)
        min_index = value_to_index[min_element]

        # Swap the index mappings before swapping the actual numbers
        temp_vti = value_to_index[min_element]
        value_to_index[min_element] = value_to_index[numbers[i]]
        value_to_index[numbers[i]] = temp_vti

        # Swap the actual min with the current element
        swap(numbers, i, min_index)

    return numbers

print sort_within_k_optimized([3, 4, 1, 2, 5], 2)