import heapq


def k_smallest_sum_pair(nums1, nums2, k):
    lookup = {v: i for i, v in enumerate(nums1)}
    min_heap = []

    for v in nums2:
        heapq.heappush(min_heap, (nums1[0]+v, nums1[0], v))

    result = []

    for i in xrange(k):
        _sum, p1, p2 = heapq.heappop(min_heap)

        result.append((p1, p2))

        next_p1 = nums1[lookup[p1]+1]
        heapq.heappush(min_heap, (next_p1 + p2, next_p1, p2))

    return result

print k_smallest_sum_pair([1, 7, 11], [2, 4, 6], 3)