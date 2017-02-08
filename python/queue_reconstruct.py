def queue_reconstruct(pairs):
    """
    406. Suppose you have a random list of people standing in a queue.
    Each person is described by a pair of integers (h, k), where h is the height of the person
    and k is the number of people in front of this person who have a height greater than or equal to h.

    Write an algorithm to reconstruct the queue.

    Example:
    Input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    Output: [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

    :param pairs: List of 2D tuples with positive integer values
    :return: Same list of 2D tuples that satisfy the above queue requirement
    """
    """
    Sort first by h value in descending order, resolving tie-breakers with the k value in ascending order
    For a Java-style comparator:
        def compare(left, right):
            if left.h == right.h:
                return left.k < right.k

            return left.h < right.h

    """
    pairs = sorted(pairs, key=lambda element: (element[0], -element[1]), reverse=True)

    # For holding values in the order they were removed from
    temp_stack = []

    result = [pairs.pop(0)]

    for h, k in pairs:

        while len(result) < k:
            result.append(temp_stack.pop())

        while len(result) > k:
            temp_stack.append(result.pop())

        result.append((h, k))

    while len(temp_stack) != 0:
        result.append(temp_stack.pop())

    print result

queue_reconstruct([(7,1), (4,4), (7,0), (5,0), (6,1), (5,2)])