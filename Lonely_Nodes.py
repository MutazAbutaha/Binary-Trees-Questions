class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_lonely_nodes(root):
    lonely_nodes = []

    def dfs(node):
        if not node:
            return

        if node.left and not node.right:
            lonely_nodes.append(node.left.val)
        elif not node.left and node.right:
            lonely_nodes.append(node.right.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return lonely_nodes

# Example usage:
# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)

print(find_lonely_nodes(root))  # Output: [4, 5]
