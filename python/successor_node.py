def successor_node(node):
    """
    Given access to a node (each node has a parent pointer too), determine
    the in-order successor node within the tree.

    :param node: The current node
    :return: The in-order successor
    """
    if node.right is not None:
        # Answer is the leftmost node in the right subtree
        current = node.right
        while current.left is not None:
            current = current.left
        return current

    # Check if successor is within the ancestor nodes
    current = node
    while current.parent is not None:
        if current.parent.left == current:
            # Answer is first parent after taking a right "hook" traversing up
            return current.parent
        current = current.parent

    # This node is the largest in the tree
    return None

