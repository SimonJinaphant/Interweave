import unittest


def unique_bst_count_2(n):
    """
    A bottom-up approach of the unique bst count problem with caching
    """
    result_cache = [0, 1]

    for i in xrange(2, n+1):

        count = 0
        for pair in xrange(i/2):
            count += 2 * result_cache[i-pair-1]

        if i % 2 == 1:
            count += result_cache[i-(i/2)-1]

        result_cache.append(count)

    return result_cache[-1]


def unique_bst_count(n):
    """
    Given n, how many structurally unique BST's (binary search trees)
    are there that store the values 1...n
    """

    if n == 0 or n == 1:
        # Base cases: An empty tree has 0 possible unique bst, and a single node tree only has itself
        return n

    """
    Consider a sequence: 1, 2, ... n

    With node 1, we can make solve a sub-problem of UniqueBST(N-1) to determine the number of possible valid bst permutation
    upon the sequence (2, 3, ... n)

    Similarly with node N we can solve the same UniqueBST(N-1) upon the sequence (1, 2, 3 ... n-1)

    There's 2 * Unique(N-1)

    Now with node 2 we can solve the subproblem of UniqueBST(N-2) upon the sequence (3, 4, ..., n)
    and same with node N-1 upon the sequence (1, 2, ..., n-2)

    For an odd N, we'll have to add an additional UniqueBST(N - (N/2) - 1) to get the middle element

    ------
    For example: The sequence 1, 2, 3 comprises of
    taking Node 1 and finding the permutations with Nodes 2 and 3 -> U(2)
    taking Node 2 and finding the permutations with Nodes 1 or 3 -> U(1)
    taking Node 3 and finding the permutations with Nodes 1 and 2 -> U(2)

    = U(2) + U(1) + U(2)
    = 2 * U(2) + U(1)

    """

    count = 0
    for pair in xrange(n/2):
        count += 2 * unique_bst_count(n - pair - 1)

    if n % 2 == 1:
        count += unique_bst_count(n - (n/2) - 1)

    return count


class TestUniqueBSTCount(unittest.TestCase):

    def test_basecase(self):
        self.assertEqual(unique_bst_count(0), 0)
        self.assertEqual(unique_bst_count(1), 1)

    def test_normal(self):
        self.assertEqual(unique_bst_count(2), 2)
        self.assertEqual(unique_bst_count(3), 5)


if __name__ == "__main__":
    unittest.main()
