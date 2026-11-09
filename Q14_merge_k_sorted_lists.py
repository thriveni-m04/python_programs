# Q14. Merge K Sorted Lists
# Merge multiple sorted linked lists into one sorted linked list.

import heapq

# Define a node for the linked list.
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


# Convert a normal list into a linked list.
def create_linked_list(values):
    dummy = Node(0)
    current = dummy

    for value in values:
        current.next = Node(value)
        current = current.next

    return dummy.next


# Convert a linked list into a normal list for displaying output.
def display_linked_list(head):
    result = []

    while head:
        result.append(head.val)
        head = head.next

    return result


# Merge all sorted linked lists.
def merge_k_lists(lists):

    heap = []

    # Insert the first node of every linked list into the heap.
    for i, node in enumerate(lists):

        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = Node(0)
    current = dummy

    while heap:

        # Remove the smallest node.
        value, i, node = heapq.heappop(heap)

        # Add it to the merged linked list.
        current.next = node
        current = current.next

        # Insert the next node from the same list.
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


# Sample input.
values = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

# Convert each list into a linked list.
lists = [create_linked_list(x) for x in values]

# Merge the linked lists.
merged = merge_k_lists(lists)

print("Merged List:", display_linked_list(merged))