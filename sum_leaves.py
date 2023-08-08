# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: TreeNode) -> int:
    sum = 0
    if not root:
        return 0

    # Check if the left child is a leaf node
    if root and not root.left and not root.right:
        sum += root.val
        return  sum 
    
    # Recursively calculate the sum for the right subtree
    
    

    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
# Create the test tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Calculate the sum of left leaves
result = sumOfLeftLeaves(root)

# Print the result
print("Sum of left leaves:", result)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def sumOfLeaves(root: TreeNode) -> int:
#     if not root:
#         return 0

#     if root and not root.left and not root.right:
#         # If the current node is a leaf, return its value
#         return root.val

#     # Recursively calculate the sum for the left and right subtrees
#     left_sum = sumOfLeaves(root.left)
#     right_sum = sumOfLeaves(root.right)

#     return left_sum + right_sum

# # Create the test tree
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

# # Calculate the sum of leaves
# result = sumOfLeaves(root)

# # Print the result
# print("Sum of leaves:", result)
