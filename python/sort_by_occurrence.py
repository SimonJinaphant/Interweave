import unittest


def sort_by_occurrence(message):
    """
    Sort a given string by the number of letter occurences

    ex: Aabb -> bbAa since 'b' appears twice, while 'A' and 'a' only appears once
        aabccc -> cccaab since 'c' appears 3 times, 'a' 2 times, ..etc..

    :param message: The message to sort
    :return: String with the most repeated characters all at the front
    """

    # Count all occurrences of a letter
    occurrences = {}
    max_occurrence = 1
    for letter in message:
        if letter in occurrences:
            occurrences[letter] += 1
            max_occurrence = max(max_occurrence,occurrences[letter])
        else:
            occurrences[letter] = 1

    # Create buckets to hold letters of 1 occurrence to @max_occurrences occurrence
    buckets = [[] for i in xrange(max_occurrence+1)]

    # Add the letters to their corresponding buckets
    for k,v in occurrences.iteritems():
        buckets[v].append(k*v)

    # Reduce the buckets into one in a reversed manner
    result = []
    for bucket in reversed(buckets):
        if len(bucket) != 0:
            result.extend(bucket)

    return "".join(result)

class TestSortByOccurrence(unittest.TestCase):
    def test_normal(self):
        self.assertEquals()
print sort_by_occurrence("Aabb")
