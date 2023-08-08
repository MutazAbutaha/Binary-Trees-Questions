# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1: TreeNode, root2: TreeNode) -> TreeNode:
    # if not root1:
    #     return root2
    # if not root2:
    #     return root1
    
    # # Merge the nodes that are overlapped
    # merged_root = TreeNode(root1.val + root2.val)
    
    # # Recursively merge left and right subtrees
    # merged_root.left = mergeTrees(root1.left, root2.left)
    # merged_root.right = mergeTrees(root1.right, root2.right)
    
    # return merged_root
    
    if not root1 and not root2 :
            return None

    if not root1 :
            return root2
    if not root2 :
            return root1

    root1.val = (root1.val + root2.val)
    root1.left = mergeTrees(root1.left,root2.left)
    root1.right = mergeTrees(root1.right,root2.right)

    return root1


# Create the first tree (root1)
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.left.left = TreeNode(5)
root1.right = TreeNode(2)

# Create the second tree (root2)
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.left.right = TreeNode(4)
root2.right = TreeNode(3)
root2.right.right = TreeNode(7)

# Merge the trees
merged_tree = mergeTrees(root1, root2)

# Function to print the tree in pre-order traversal
def print_tree_in_preorder(root):
    if root:
        print(root.val, end=" ")
        print_tree_in_preorder(root.left)
        print_tree_in_preorder(root.right)

# Print the merged tree in pre-order traversal
print("Merged tree in pre-order:")
print_tree_in_preorder(merged_tree)
