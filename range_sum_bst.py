class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def range_sum_bst(root, low, high):
    if root is None:
        return 0

    # If the current node value is outside the range, we skip it and go to the subtrees.
    if root.val < low:
        return range_sum_bst(root.right, low, high)
    elif root.val > high:
        return range_sum_bst(root.left, low, high)

    # If the current node value is within the range, we include it in the sum and explore both subtrees.
    return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)

# Example BST: 
#       10
#      /  \
#     5   15
#    / \    \
#   3   7   18

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

low = 7
high = 15
result = range_sum_bst(root, low, high)
print(result)  # Output will be 32 (7 + 10 + 15)
