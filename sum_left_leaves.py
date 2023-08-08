# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0

    # Check if the left child is a leaf node
    if root.left and not root.left.left and not root.left.right:
        left_sum = root.left.val
    else:
        left_sum = sumOfLeftLeaves(root.left)

    # Recursively calculate the sum for the right subtree
    right_sum = sumOfLeftLeaves(root.right)

    return left_sum + right_sum
# Create the test tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the sum of left leaves
result = sumOfLeftLeaves(root)

# Print the result
print("Sum of left leaves:", result)
