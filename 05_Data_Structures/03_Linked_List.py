# Linked List:

# A linked list is a linear data structure that consists of a sequence of nodes, each containing data and a reference (or pointer) to the next node in the list. Unlike arrays, which store elements in contiguous memory locations, linked lists can be scattered throughout memory, connected by pointers.

# Key Concepts:

# - **Node:** A basic building block of a linked list. Each node contains:
#     - **Data:** The actual value stored in the node.
#     - **Next Pointer:** A reference to the next node in the list. The last node's next pointer typically points to `None` (or `NULL`).

# - **Head:** A pointer to the first node in the linked list.

# - **Tail:** A pointer to the last node in the linked list.

# Types of Linked Lists:

# - **Singly Linked List:** Each node has a pointer to the next node only.
# - **Doubly Linked List:** Each node has pointers to both the next and previous nodes.
# - **Circular Linked List:** The last node's next pointer points back to the first node, forming a circle.

# Advantages of Linked Lists:

# - **Dynamic Size:** Linked lists can grow or shrink dynamically as needed, unlike arrays, which have a fixed size.
# - **Efficient Insertion and Deletion:** Inserting or deleting elements in a linked list is generally faster than in arrays, especially in the middle of the list.
# - **Memory Efficiency:** Linked lists can utilize memory more efficiently than arrays, as they don't require contiguous memory allocation.

# Disadvantages of Linked Lists:

# - **Random Access:** Accessing a specific element in a linked list requires traversing the list from the head, which can be slow for large lists.
# - **Pointer Complexity:** Managing pointers can be more complex than working with arrays.

# Implementation:

# Here's a simple Python implementation of a singly linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Usage:

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)

print("Linked list:", end=" ")
linked_list.print_list()  # Output: Linked list: 10 20 30

# Applications:

# - **Implementing Stacks and Queues:** Linked lists provide a natural way to implement stacks and queues.
# - **Dynamic Memory Allocation:** Linked lists are used in memory management systems for allocating and deallocating memory blocks.
# - **Graph Data Structures:** Linked lists are used to represent edges in graph data structures.
# - **Polynomial Representation:** Linked lists can be used to represent polynomials.
# - **Hash Tables:** Linked lists are used to resolve collisions in hash tables.

# Advanced Concepts:

# - **Doubly Linked Lists:** Allow traversal in both directions (forward and backward).
# - **Circular Linked Lists:** The last node points back to the first node, creating a loop.
# - **Sorted Linked Lists:** Elements are maintained in a sorted order.
# - **Linked List Operations:** Insertion, deletion, searching, reversing, merging, etc.

# Linked lists are a versatile data structure with various applications in computer science. Understanding their concepts and implementation is essential for building efficient and dynamic data structures.
#
#
#