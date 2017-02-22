import heapq


def median_k_sorted(list_of_lists, total_elements):
    current_pointers = []
    min_heap = []

    for list_index, list in enumerate(list_of_lists):
        current_pointers.append(0)
        min_heap.append((list[0], list_index))

    heapq.heapify(min_heap)

    for i in xrange(total_elements/2):
        _, list_no = heapq.heappop(min_heap)

        current_pointers[list_no] += 1
        if current_pointers[list_no] == len(list_of_lists[list_no]):
            continue

        heapq.heappush(min_heap, (list_of_lists[list_no][current_pointers[list_no]] ,list_no))

    median_left, _li = heapq.heappop(min_heap)

    if total_elements % 2 == 0:
        median_right, _ri = heapq.heappop(min_heap)
        return (median_left + median_right) / 2
    else:
        return median_left

print median_k_sorted([[1,2,3],[4,5,6],[7,8,9]], 9)