# Question 10: Kth Smallest Element in a BST
# Given the root of a Binary Search Tree and an integer k,
# find the kth smallest value in the tree.
# K is 1-indexed.

# Create a class for tree nodes
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Construct the sample BST
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

k = 5

# Store inorder traversal values
values = []


# Perform inorder traversal
def inorder(node):

    if node is None:
        return

    # Visit left subtree
    inorder(node.left)

    # Visit current node
    values.append(node.val)

    # Visit right subtree
    inorder(node.right)


# Start traversal
inorder(root)

# Find the kth smallest element
if 1 <= k <= len(values):
    print("Kth Smallest Element:", values[k - 1])
else:
    print("Invalid value of k")

