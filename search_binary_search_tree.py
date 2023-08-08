# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root: TreeNode, val: int) -> TreeNode:
    if not root:
        return None
    
    if root.val == val:
        return root
    
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)
# Create the test BST
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Function to print the tree in in-order traversal
def print_tree_in_order(root):
    if not root:
        return

    print_tree_in_order(root.left)
    print(root.val, end=" ")
    print_tree_in_order(root.right)

# Print the original BST in in-order traversal
print("Original BST in in-order:")
print_tree_in_order(root)
print()

# Find the node with value 3
val = 7
subtree_with_val = searchBST(root, val)

# Print the subtree with value 3 in in-order traversal
print("Subtree with value", val, "in in-order:")
print_tree_in_order(subtree_with_val)
