import unittest


def levenshtein(s, t):
    """
    Levenshtein Distance measures the dissimilarity between 2 strings by giving the minimal number of 
    character insertion, deletion, and substitution required to transform one string to the other.

    The distance between 'car' and 'car' is 0 because they are the same
    The distance between 'car' and 'bar' is 1 because the first letter differs
    The distance between 'friend' and 'freinds' is 3 because of 'ie' vs 'ei' and the extra 's' 

    Reference: 
    - https://semanti.ca/blog/?an-introduction-into-approximate-string-matching
    - https://en.wikipedia.org/wiki/Levenshtein_distance
    """
    m = len(s)
    n = len(t)
    if m == 0:
        return n
    if n == 0:
        return m

    matrix = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
    for i in xrange(0, m+1):
        matrix[i][0] = i
    for j in xrange(0, n+1):
        matrix[0][j] = j

    for i in xrange(1, m+1):
        s_i = s[i - 1]
        for j in xrange(1, n+1):
            t_j = t[j - 1]

            deletion = matrix[i-1][j]+1
            insertion = matrix[i][j-1]+1
            substitution = matrix[i-1][j-1] + (0 if s_i == t_j else 1)

            matrix[i][j] = min(deletion, insertion, substitution)

    return matrix[m][n]


class TestLevenshtein(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(levenshtein("car", "bar"), 1)
        self.assertEqual(levenshtein("friend", "freinds"), 3)
        self.assertEqual(levenshtein("car", "freinds"), 7)


if __name__ == "__main__":
    unittest.main()
