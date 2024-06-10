# Queue is a linear data structure that follows the FIFO (First-In, First-Out) principle. It's like a queue of people waiting in line, where the person who arrived first is the first to be served.

# Key Operations:

# - **Enqueue:** Adds an element to the rear of the queue.
# - **Dequeue:** Removes and returns the element at the front of the queue.
# - **Peek:** Returns the element at the front of the queue without removing it.
# - **IsEmpty:** Checks if the queue is empty.
# - **Size:** Returns the number of elements in the queue.

# Implementation:

# Queues can be implemented using various data structures, such as:

# - **Lists:** Python lists can be used to represent queues, with the `append()` method for enqueueing and the `pop(0)` method for dequeueing.
# - **Deque (Double-Ended Queue):** The `collections.deque` class provides a more efficient implementation of queues, allowing for both enqueueing and dequeueing from both ends.

# Example using Lists:

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Usage:

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(f"Queue size: {queue.size()}")  # Output: Queue size: 3
print(f"Front element: {queue.peek()}")  # Output: Front element: 10
print(f"Dequeued element: {queue.dequeue()}")  # Output: Dequeued element: 10
print(f"Queue size: {queue.size()}")  # Output: Queue size: 2

# Applications:

# - **Task Scheduling:**  Used to manage tasks in a system, processing them in the order they were received.
# - **Message Queues:**  Used for asynchronous communication between different parts of a system.
# - **Buffering:**  Used to temporarily store data before it's processed.
# - **Print Queue:**  Used to manage print jobs in a printer.
# - **Breadth-First Search (BFS) Algorithm:**  Used in graph traversal.
#
#
#