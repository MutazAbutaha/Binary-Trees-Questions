class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_second_minimum_value(root):
    def dfs(node):
        nonlocal first_min, second_min
        
        if node:
            if first_min is None:
                first_min = node.val
            elif first_min > node.val:
                second_min = first_min
                first_min = node.val
            elif first_min < node.val and (second_min is None or node.val < second_min):
                second_min = node.val
            
            dfs(node.left)
            dfs(node.right)

    first_min, second_min = None, None
    dfs(root)

    if second_min is None:
        return -1

    return second_min

# Example usage:
# Create the binary tree
root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

print(find_second_minimum_value(root))  # Output: 5
