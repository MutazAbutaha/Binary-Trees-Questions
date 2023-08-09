class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    
    return root

# Example usage:
# Create a binary search tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

# Insert a new value (e.g., 8) into the BST
new_value = 1
root = insert_into_bst(root, new_value)

# Now `root` represents the updated binary search tree with the new value.
def print_tree_in_order(root):
    if not root:
        return None

    print_tree_in_order(root.left)
    print(root.val, end=" ")
    print_tree_in_order(root.right)
print_tree_in_order(root)