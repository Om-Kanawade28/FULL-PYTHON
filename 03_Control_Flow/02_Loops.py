#
# Loops are fundamental control flow structures in programming that allow you to repeat a block of code multiple times. They are essential for automating tasks, processing data, and creating iterative algorithms.

# 1. `for` Loop:
#   - The `for` loop is used to iterate over a sequence (like a list, tuple, string, or range). It executes the loop body for each item in the sequence.


# Example 1: Iterating over a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
#output:-
# 1
# 2
# 3
# 4
# 5

# Example 2: Iterating over a string
name = "Python"
for letter in name:
    print(letter)
#output:-
# P
# y
# t
# h
# o
# n

# Example 3: Iterating over a range
for i in range(1, 6):
    print(i)
#output:-
# 1
# 2
# 3
# 4
# 5

# 2. `while` Loop:
#   - The `while` loop executes a block of code repeatedly as long as a specified condition is true.


# Example 1: Counting to 10
count = 1
while count <= 10:
    print(count)
    count += 1
#output:-
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Example 2: Getting user input until a specific value is entered
user_input = ""
while user_input != "quit":
    user_input = input("Enter a value (or 'quit' to exit): ")
    print(f"You entered: {user_input}")
#output:-
# Enter a value (or 'quit' to exit): hello
# You entered: hello
# Enter a value (or 'quit' to exit): world
# You entered: world
# Enter a value (or 'quit' to exit): quit
# You entered: quit

# 3. `break` Statement:
#   - The
#     `break` statement is used to exit a loop prematurely. It terminates the loop immediately, regardless of whether the loop condition is still true.


# Example 1: Breaking out of a `for` loop
for i in range(1, 11):
    if i == 5:
        break
    print(i)
#output:-
# 1
# 2
# 3
# 4

# Example 2: Breaking out of a `while` loop
count = 1
while True:
    print(count)
    count += 1
    if count > 5:
        break
#output:-
# 1
# 2
# 3
# 4
# 5

# 4. `continue` Statement:
#   - The `continue` statement skips the current iteration of a loop and jumps to the next iteration.


# Example 1: Skipping even numbers in a `for` loop
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
#output:-
# 1
# 3
# 5
# 7
# 9

# Example 2: Skipping negative numbers in a `while` loop
count = 1
while count <= 10:
    if count < 0:
        continue
    print(count)
    count += 1
#output:-
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# 5. Nested Loops:
#   - You can nest loops within other loops to create more complex iteration patterns.


# Example: Printing a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)
#output:-
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# --------------------
# 
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# --------------------
# 
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# --------------------
# 
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# --------------------
# 
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# --------------------

# 6. Looping with `else` Block:
#   - The `else` block in a loop is executed only if the loop completes normally (without encountering a `break` statement).


# Example: Searching for a value in a list
numbers = [1, 2, 3, 4, 5]
search_value = 3
for number in numbers:
    if number == search_value:
        print(f"Found {search_value} in the list.")
        break
else:
    print(f"{search_value} not found in the list.")
#output:-
# Found 3 in the list.

# 7. Looping with `enumerate()`:
#   - The `enumerate()` function is useful for iterating over a sequence while also getting the index of each item.


# Example: Printing items with their indices
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
#output:-
# Index 0: apple
# Index 1: banana
# Index 2: orange

# 8. Looping with `zip()`:
#   - The `zip()` function is used
#     to iterate over multiple sequences simultaneously.


# Example: Combining two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
#output:-
# Alice is 25 years old.
# Bob is 30 years old.
# Charlie is 28 years old.

# Remember that loops are essential for creating repetitive actions and processing data efficiently in your Python programs. Choose the appropriate loop type based on your specific needs and use `break`, `continue`, and `else` blocks to control the flow of execution within your loops.
#
#

