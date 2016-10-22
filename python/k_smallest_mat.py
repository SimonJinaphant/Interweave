import unittest
from math import sqrt, pow


def k_smallest_matrix(matrix, k):
    """
    Given a n x n matrix where each of the rows and columns are sorted in ascending order,
    find the kth smallest element in the matrix.

    :param matrix: A square matrix of size n x n in sorted order for its rows and cols
    :param k: The kth-smallest element to look for

    :return: An k-th smallest element in the matrix.
    """
    sqrt_k = sqrt(k)
    cut_off = int(sqrt_k)

    if sqrt_k == float(cut_off):
        # K is a perfect square so we'll return the diagonal
        return matrix[cut_off-1][cut_off-1]

    # The answer is within the subvectors
    cut_off_row = 0
    cut_off_col = 0
    current_number = None;

    # Find how many elements we need to check until we reach the new k value
    until_k = k - int(pow(cut_off, 2.0))

    while until_k != 0:
        if matrix[cut_off][cut_off_col] < matrix[cut_off_row][cut_off]:
            current_number = matrix[cut_off][cut_off_col]
            cut_off_col += 1
        else:
            current_number = matrix[cut_off_row][cut_off]
            cut_off_row += 1

        until_k -= 1

    return current_number


class TestKSmallestMatrix(unittest.TestCase):

    def test_normal(self):

        matrix = [[1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]]

        self.assertEqual(k_smallest_matrix(matrix, 8), 13)
        self.assertEqual(k_smallest_matrix(matrix, 1), 1)
        self.assertEqual(k_smallest_matrix(matrix, 9), 15)
        
        #self.assertEqual(k_smallest_matrix(matrix, 5), 11)


if __name__ == "__main__":
    unittest.main()