class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def compare_trees(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val :
        return False
    return compare_trees(root1.left, root2.left) and compare_trees(root1.right, root2.right)

# Create the first tree
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(2)

# Create the second tree
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

# Check if the two trees are the same
result = compare_trees(root1, root2)

# Print the result
print("Are the trees the same?", result)
