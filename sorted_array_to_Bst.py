class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    print(mid)
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root

sorted_array = [1, 2, 3, 4, 5, 6, 7] 
bst_root = sorted_array_to_bst(sorted_array)
# print(bst_root)
# Now `bst_root` represents the root of the binary search tree.
def print_tree_in_preorder(root):
    if root:
        print(root.val, end=" ")
        print_tree_in_preorder(root.left)
        print_tree_in_preorder(root.right)

# Print the merged tree in pre-order traversal
print("Merged tree in pre-order:")
print_tree_in_preorder(bst_root)
