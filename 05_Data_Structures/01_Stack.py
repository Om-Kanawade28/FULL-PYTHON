# Stack is a linear data structure that follows the LIFO (Last-In, First-Out) principle. It's like a stack of plates, where you can only add or remove plates from the top.

# Key Operations:

# - **Push:** Adds an element to the top of the stack.
# - **Pop:** Removes and returns the element at the top of the stack.
# - **Peek:** Returns the element at the top of the stack without removing it.
# - **IsEmpty:** Checks if the stack is empty.
# - **Size:** Returns the number of elements in the stack.

# Implementation:

# Stacks can be implemented using various data structures, such as:

# - **Lists:** Python lists can be used to represent stacks, with the `append()` method for pushing and the `pop()` method for popping.
# - **Queues:** Stacks can also be implemented using queues, but it's less efficient due to the FIFO (First-In, First-Out) nature of queues.

# Example using Lists:

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Usage:

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(f"Stack size: {stack.size()}")  # Output: Stack size: 3
print(f"Top element: {stack.peek()}")  # Output: Top element: 30
print(f"Popped element: {stack.pop()}")  # Output: Popped element: 30
print(f"Stack size: {stack.size()}")  # Output: Stack size: 2

# Applications:

# - **Function Call Stack:**  Keeps track of active
#   function calls.
# - **Undo/Redo Functionality:**  Stores actions for undoing or redoing operations.
# - **Expression Evaluation:**  Used in evaluating mathematical expressions.
# - **Browser History:**  Stores visited web pages.
# - **Memory Management:**  Used in allocating and deallocating memory.
#
#