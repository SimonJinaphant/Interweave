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

    '''
    Create a m+1 by n+1 matrix, letting the m[0][0] denote the distance between 2 empty strings
    In the entire 1st column, we compare one string against the sub-problem of an empty string
    In the entire 2nd column, we compare that string against the sub-problem of a string containing the first letters of the other string
    In the entire 3rd column..etc, we compare that string against the sub-problem of a string containing the first 2 letters of the other string
    Similarly for the entire rows...

    In the entire first column, since we're comparing against an empty string, the distance for each row in that column 
    will be incremental from 0 to the length of that string. Same for the entire first row.
    '''
    matrix = [[0 for j in xrange(n+1)] for i in xrange(m+1)]
    for i in xrange(0, m+1):
        matrix[i][0] = i
    for j in xrange(0, n+1):
        matrix[0][j] = j

    '''
    Now we compare the rest of the matrix
    At each slot we consider 3 possible case:
    1. If the current letter in column string is removed (Deletion), obtained from looking one row up
    2. If the current letter in row string t is removed (Insertion, or deleting from the other string); obtained from looking one column behind
    3. If the current letters in both are removed (Substitution), obtain from looking diagonally behind.
    '''
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
