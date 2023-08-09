class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def min_node_value(root):
    if not root:
        return float('-inf')

    left_max = min_node_value(root.left)
    right_max = min_node_value(root.right)

    current_max = root.value
    if left_max > current_max:
        current_max = left_max
    if right_max > current_max:
        current_max = right_max

    return current_max

    
    

# Helper function to create a sample binary tree
def create_binary_tree():
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(20)
    root.right.right = TreeNode(8)
    return root

# Test the function with a sample binary tree
bst_root = create_binary_tree()

print("Minimum node value in the binary tree:", min_node_value(bst_root))  # Output: 8
