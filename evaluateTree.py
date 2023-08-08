class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluate(root):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == 1  # True if the leaf node has value 1 (True), False if value is 0 (False).

    left_eval = evaluate(root.left)
    right_eval = evaluate(root.right)

    if root.val == 2:  # Boolean OR operation
        return left_eval or right_eval
    elif root.val == 3:  # Boolean AND operation
        return left_eval and right_eval
    else:
        return False  # For any other non-leaf node value (2 or 3), return False.

# Example usage:
# Create the full binary tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)

print(evaluate(root))  # Output: True
