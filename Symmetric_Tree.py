class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def is_symmetric(root):
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
    return is_mirror(root.left, root.right)

# Example usage:
# Create a symmetric tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(is_symmetric(root))  # Output: True

# Create a non-symmetric tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)

print(is_symmetric(root))  # Output: False

