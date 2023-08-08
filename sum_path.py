# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    if not root:
        return False

    # Check if the current node is a leaf node
    if not root.left and not root.right:
        return targetSum == root.val

    # Recursively check the left and right subtrees
    remaining_sum = targetSum - root.val
    return hasPathSum(root.left, remaining_sum) or hasPathSum(root.right, remaining_sum)

# Create the test binary tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

# Check if there exists a root-to-leaf path with sum 22
targetSum = 27
result = hasPathSum(root, targetSum)

# Print the result
print("Has path with sum", targetSum, "?", result)
