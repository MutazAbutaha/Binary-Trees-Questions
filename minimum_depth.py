# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0

    # If the current node is a leaf, return 1
    if not root.left and not root.right:
        return 1

    # Recursively find the minimum depth of left and right subtrees
    left_depth = minDepth(root.left)
    right_depth = minDepth(root.right)

    # If one of the subtrees is empty, consider the depth of the non-empty one
    if not root.left:
        return right_depth + 1
    if not root.right:
        return left_depth + 1

    # If both subtrees are not empty, return the minimum depth plus 1 for the current node
    return left_depth + 1 if left_depth < right_depth else right_depth + 1

# Create the test binary tree

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Find the minimum depth of the binary tree
result = minDepth(root)

# Print the result
print("Minimum depth of the tree:", result)
