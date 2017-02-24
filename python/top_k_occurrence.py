import unittest


def top_k_occurrence(data, k):
    """
    Given a non-empty array of integers, return the k most frequent elements.

    For example,
    Given [1,1,1,2,2,3] and k = 2, return [1,2].

    :param data: Array of hashable items
    :param k: The minimum occurrence, an integer > 0
    :return: Array of elements that occurs at minimum k times
    """

    # Count the occurrences of all elements
    occurrences = {}
    max_occurrence = 1
    for d in data:
        if d in occurrences:
            occurrences[d] += 1
            max_occurrence = max(max_occurrence, occurrences[d])
        else:
            occurrences[d] = 1

    # Create buckets and put similar occurrences in the same bucket
    buckets = [[] for i in xrange(max_occurrence)]
    for data_key, data_occurrence in occurrences.iteritems():
        buckets[data_occurrence - 1].append(data_key)

    # Return the buckets numbered >= k
    result = []
    for bucket in buckets[k-1:]:
        result.extend(bucket)

    return result


class TopKOccurrenceTest(unittest.TestCase):
    def test_normals(self):
        self.assertItemsEqual(top_k_occurrence([1,2,3,2,1,1], 2), [1,2])
        self.assertItemsEqual(top_k_occurrence([1,2,3,2,1,1], 3), [1])

    def test_edge(self):
        self.assertItemsEqual(top_k_occurrence([1,2], 4), [])
        self.assertItemsEqual(top_k_occurrence([], 1), [])


if __name__ == "__main__":
    unittest.main()
