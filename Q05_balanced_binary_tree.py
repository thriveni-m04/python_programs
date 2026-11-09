# Question 5: Balanced Binary Tree
# Given the root of a binary tree, determine whether
# the tree is height-balanced.
# A tree is balanced if the height difference between
# its left and right subtrees is at most 1 at every node.

# Create a class for tree nodes
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


# Construct a sample binary tree
root = TreeNode(3)

root.left = TreeNode(9)
root.right = TreeNode(20)

root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# Calculate height and check balance together
def check_balance(node):

    # An empty node has height 0
    if node is None:
        return 0

    # Find the height of the left subtree
    left_height = check_balance(node.left)

    # If left subtree is unbalanced
    if left_height == -1:
        return -1

    # Find the height of the right subtree
    right_height = check_balance(node.right)

    # If right subtree is unbalanced
    if right_height == -1:
        return -1

    # Check the height difference
    if abs(left_height - right_height) > 1:
        return -1

    # Return the height of the current node
    return 1 + max(left_height, right_height)


# Check whether the tree is balanced
if check_balance(root) != -1:
    print("Balanced Binary Tree: True")
else:
    print("Balanced Binary Tree: False")

