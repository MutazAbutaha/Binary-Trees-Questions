# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    # Recursively find the maximum depth of left and right subtrees
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # Compare left_depth and right_depth to return the greater value plus 1 for the current node
    if left_depth > right_depth:
        return left_depth + 1
    else:
        return right_depth + 1

# Create the test binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(7)
# Find the maximum depth of the binary tree
result = maxDepth(root)

# Print the result
print("Maximum depth of the tree:", result)
