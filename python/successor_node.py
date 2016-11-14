def successor_node(node):
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

