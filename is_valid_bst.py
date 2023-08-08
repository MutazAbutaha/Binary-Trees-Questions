class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root):
    def helper(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        value = node.value
        if value <= lower or value >= upper:
            return False

        if not helper(node.left, lower, value):
            return False
        if not helper(node.right, value, upper):
            return False

        return True

    return helper(root)

# Helper function to create a sample binary tree
def create_binary_tree():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    return root

# Helper function to create a sample binary tree which is not a BST
def create_non_bst():
    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(2)
    return root

# Test the function with a sample binary tree
bst_root = create_binary_tree()
non_bst_root = create_non_bst()

print("Is the given binary tree a valid BST?", is_valid_bst(bst_root))  # Output: True
print("Is the given binary tree a valid BST?", is_valid_bst(non_bst_root))  # Output: False
