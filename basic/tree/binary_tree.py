def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = root.left, root.right
    invert_tree(root.left)
    invert_tree(root.right)

    return root
