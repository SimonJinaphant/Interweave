import heapq


def median_k_sorted(list_of_lists, total_elements):
    """
    Determine the median of k sorted arrays

    :param list_of_lists: Collection containing k lists of numbers
    :param total_elements: Total amount of elements in all k lists
    :return: The median of all k sorted arrays
    """

    """
    This is similar to trying to merge all k arrays into one array and finding the median
    We can find the median by observing the smallest n/2 elements (n is the total # of elements) as we try to "merge"
    in the sublists.

    """
    # Keep track of where each list's current pointer is at
    current_pointers = []
    # Keep track of the smallest elements, getting ready to replace the smallest one
    min_heap = []

    for list_index, list in enumerate(list_of_lists):
        current_pointers.append(0)
        min_heap.append((list[0], list_index))

    heapq.heapify(min_heap)

    for i in xrange(total_elements/2):
        # Remove the smallest element and add the next element from the same sublist
        _, list_no = heapq.heappop(min_heap)

        current_pointers[list_no] += 1
        if current_pointers[list_no] == len(list_of_lists[list_no]):
            # Edge case: we've exhausted the current sublist
            continue

        heapq.heappush(min_heap, (list_of_lists[list_no][current_pointers[list_no]] ,list_no))

    # Now we have atleast k elements in our heap, with the top one being the middle element
    median_left, _li = heapq.heappop(min_heap)

    if total_elements % 2 == 0:
        median_right, _ri = heapq.heappop(min_heap)
        return (median_left + median_right) / 2
    else:
        return median_left

print median_k_sorted([[1,2,3],[4,5,6],[7,8,9]], 9)