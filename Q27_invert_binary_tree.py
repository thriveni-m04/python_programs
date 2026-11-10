# Q27. Invert Binary Tree
# Swap the left and right children of every node.

# Create a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Invert the binary tree
def invert_tree(root):

    if root is None:
        return None

    # Swap left and right children
    root.left, root.right = root.right, root.left

    # Invert left and right subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# Print the tree in level order
def print_tree(root):

    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        print(node.value, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


# Create the binary tree
root = Node(4)
root.left = Node(2)
root.right = Node(7)

root.left.left = Node(1)
root.left.right = Node(3)

root.right.left = Node(6)
root.right.right = Node(9)

print("Original Tree:")
print_tree(root)

# Invert the tree
invert_tree(root)

print("\nInverted Tree:")
print_tree(root)

