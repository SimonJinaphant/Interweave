import Queue


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def max_tree_row(root):
    """
    Find the largest value in each row of a binary tree.

    ie:
        Input:

              1
             / \
            3   2
           / \   \
          5   3   9

        Output: [1, 3, 9]

    :param root: The root of the binary tree
    :return: The maximum values in each row of the tree
    """

    """
    Perform a modified BFS that keeps track of when we switch into another row
        At each row we compare a node with the current minimum value we've found on that row

        Due to the nature of BFS we don't go into the next row until all of the nodes in the current
        row has been analysed
    """
    row_max = []
    current_row_max = None

    open_list = Queue.Queue()
    open_list.put(root)
    current_level = 1
    next_level = 0

    while not open_list.empty():
        current_node = open_list.get()
        current_level -= 1

        # Record the current minimum value we've seen so far
        if current_row_max is None:
            current_row_max = current_node.value
        else:
            current_row_max = max(current_row_max, current_node.value)

        # Look for child nodes to analyse later after this row is done
        if current_node.left is not None:
            open_list.put(current_node.left)
            next_level += 1

        if current_node.right is not None:
            open_list.put(current_node.right)
            next_level += 1

        # We've reached the end of the row
        if current_level == 0:
            row_max.append(current_row_max)
            current_row_max = None

            current_level = next_level
            next_level = 0

    return row_max

r = Node(1)
rl = r.left = Node(3)
rr = r.right = Node(2)
rl.left = Node(5)
rl.right = Node(3)
rr.right = Node(9)

print max_tree_row(r)