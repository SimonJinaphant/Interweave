import heapq


def k_smallest_sum_pair(nums1, nums2, k):
    """
    373. You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
    Define a pair (u,v) which consists of one element from the first array and one element from the second array.

    Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

    Ex:
        Given nums1 = [1,7,11]
        nums2 = [2,4,6]
        k = 3

        Return: [ [1,2], [1,4], [1,6] ]

    :param nums1: The first array of ascending integers
    :param nums2: The second array of ascending integers
    :param k: The amount of min sum pairs to find

    :return: An array of sum pairs which are the smallest sums
    """
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