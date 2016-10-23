import unittest
import heapq


def k_smallest_matrix(matrix, k):
    """
    Given a n x n matrix where each of the rows and columns are sorted in ascending order,
    find the kth smallest element in the matrix.

    :param matrix: A square matrix of size n x n in sorted order for its rows and cols
    :param k: The kth-smallest element to look for

    :return: An k-th smallest element in the matrix.
    """

    # Take the entire first row and heapify it
    open_list = [(matrix[y][x], y, x) for x in xrange(len(matrix)) for y in xrange(len(matrix))]
    heapq.heapify(open_list)
    current_min = None

    # Take the min element and possibly enqueue the element below it
    while k != 0:
        current_min, current_y, current_x = heapq.heappop(open_list)

        if y < len(matrix):
            heapq.heappush(open_list, (matrix[y][x], current_y, current_x))

        k -= 1
    return current_min


class TestKSmallestMatrix(unittest.TestCase):

    def test_normal(self):

        matrix = [[1, 5, 9],
                [10, 11, 13],
                [12, 13, 15]]

        self.assertEqual(k_smallest_matrix(matrix, 8), 13)
        self.assertEqual(k_smallest_matrix(matrix, 1), 1)
        self.assertEqual(k_smallest_matrix(matrix, 5), 11)
        self.assertEqual(k_smallest_matrix(matrix, 9), 15)

if __name__ == "__main__":
    unittest.main()