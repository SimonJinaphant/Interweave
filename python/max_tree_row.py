import Queue


class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


def max_tree_row(root):
    row_max = []
    open_list = Queue.Queue()
    open_list.put(root)
    current_level = 1
    next_level = 0

    this_row_max = None

    while not open_list.empty():
        current_node = open_list.get()
        current_level -= 1

        if this_row_max is None:
            this_row_max = current_node.value
        else:
            this_row_max = max(this_row_max, current_node.value)

        if current_node.left is not None:
            open_list.put(current_node.left)
            next_level += 1

        if current_node.right is not None:
            open_list.put(current_node.right)
            next_level += 1

        if current_level == 0:
            row_max.append(this_row_max)
            this_row_max = None
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