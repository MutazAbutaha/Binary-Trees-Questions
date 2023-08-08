# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively invert the left and right subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root
# Create the test tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Function to print the tree in level-order traversal
def print_tree_in_level_order(root):
    if not root:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Print the original tree in level-order traversal
print("Original tree in level-order:")
print_tree_in_level_order(root)
print()

# Invert the tree
inverted_tree = invertTree(root)

# Print the inverted tree in level-order traversal
print("Inverted tree in level-order:")
print_tree_in_level_order(inverted_tree)
