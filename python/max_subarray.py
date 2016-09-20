import unittest


def max_subarray(numbers):
    """Determine the largest contiguous sub-array which has the largest sum
    :param numbers: An array of integer numbers
    :return: An sub-array of numbers which produces the largest sum
    """
    lookup = [None] * len(numbers)
    lookup[0] = numbers[0]

    end = 0
    for i in xrange(1, len(numbers)):
        lookup[i] = numbers[i] + lookup[i-1]
        if lookup[i] > lookup[end]:
            end = i

    start = lookup.index(min(lookup)) + 1

    return numbers[start:end+1]


def max_subarray2(numbers):

    sum_at_position = [None] * (len(numbers)+1)
    sum_at_position[0] = 0

    max_sum_index = 0
    for index, value in enumerate(numbers):
        sum_at_position[index+1] = sum_at_position[index] + value
        if sum_at_position[index+1] > sum_at_position[max_sum_index]:
            max_sum_index = index+1

    start = sum_at_position.index(min(sum_at_position))

    return numbers[start : max_sum_index]


def saif_sub(arr):

    # Check to see if array is length 0
    if len(arr)==0:
        return 0

    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0]

    # For every element in array
    for num in arr[1:]:

        # Set current sum as the higher of the two
        current_sum = max(current_sum+num, num)

        # Set max as the higher between the currentSum and the current max
        max_sum = max(current_sum, max_sum)

    return max_sum

class TestMaxSubarray(unittest.TestCase):
    '''def test_normal(self):
        #self.assertEquals(max_subarray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]), [4, -1, 2, 1])
        #self.assertEquals(max_subarray2([-2, -3, 4, -1, -2, 1, 5, -3]), [4, -1, -2, 1, 5])
        #self.assertEqual(max_subarray2([1, 2, -1, 3, 4, -1]), [1, 2, -1, 3, 4])
        self.assertEqual(max_subarray2([-1, 1]), [1])
        #self.assertEqual(max_subarray2([-1, 3, 4, -1]), [3,4])'''

    def test_saif(self):
        self.assertEquals(saif_sub([-2, 1, -3, 4, -1, 2, 1, -5, 4]), sum([4, -1, 2, 1]))
        self.assertEquals(saif_sub([-2, -3, 4, -1, -2, 1, 5, -3]), sum([4, -1, -2, 1, 5]))
        self.assertEqual(saif_sub([1, 2, -1, 3, 4, -1]), sum([1, 2, -1, 3, 4]))
        self.assertEqual(saif_sub([-1, 1]), sum([1]))
        self.assertEqual(saif_sub([-1, 3, 4, -1]), sum([3,4]))

if __name__ == "__main__":
    unittest.main()