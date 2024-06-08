# Lists are mutable, ordered sequences of elements. They are enclosed in square brackets ([ ]).
# Lists can contain elements of different data types.

# Methods:
# - append(): Adds an element to the end of the list.
# - insert(): Inserts an element at a specified index.
# - remove(): Removes the first occurrence of an element.
# - pop(): Removes and returns the element at a specified index (or the last element if no index is provided).
# - sort(): Sorts the list in ascending order.
# - reverse(): Reverses the order of elements in the list.
# - index(): Returns the index of the first occurrence of an element.
# - count(): Returns the number of occurrences of an element.
# - extend(): Appends the elements of another iterable to the end of the list.

# Properties:
# - len(): Returns the length of the list.
# - min(): Returns the minimum element in the list.
# - max(): Returns the maximum element in the list.
# - sum(): Returns the sum of all elements in the list.

# Examples:
# Create a list
my_list = [1, 2, 3, "apple", "banana", True]

# Add an element to the end
my_list.append("cherry")
print(my_list)  # Output: [1, 2, 3, 'apple', 'banana', True, 'cherry']

# Insert an element at index 2
my_list.insert(2, "orange")
print(my_list)  # Output: [1, 2, 'orange', 3, 'apple', 'banana', True, 'cherry']

# Remove the first occurrence of "apple"
my_list.remove("apple")
print(my_list)  # Output: [1, 2, 'orange', 3, 'banana', True, 'cherry']

# Remove and return the element at index 1
popped_element = my_list.pop(1)
print(popped_element)  # Output: 2
print(my_list)  # Output: [1, 'orange', 3, 'banana', True, 'cherry']

# Sort the list in ascending order
my_list.sort()
print(my_list)  # Output:
# [1, 3, 'banana', 'cherry', 'orange', True]

# Reverse the order of elements
my_list.reverse()
print(my_list)  # Output:
# [True, 'orange', 'cherry', 'banana', 3, 1]

# Get the index of the first occurrence of "cherry"
index = my_list.index("cherry")
print(index)  # Output: 2

# Count the number of occurrences of "banana"
count = my_list.count("banana")
print(count)  # Output: 1

# Extend the list with another list
another_list = [4, 5, 6]
my_list.extend(another_list)
print(my_list)  # Output:
# [True, 'orange', 'cherry', 'banana', 3, 1, 4, 5, 6]

# Get the length of the list
length = len(my_list)
print(length)  # Output: 9

# Get the minimum element in the list
minimum = min(my_list)
print(minimum)  # Output: 1

# Get the maximum element in the list
maximum = max(my_list)
print(maximum)  # Output: 6

# Get the sum of all elements in the list
total = sum(my_list)
print(total)  # Output: 26

# List slicing:
# You can access individual elements or sublists using slicing.
# Syntax: list[start:end:step]

# Examples:
# Get the first element
first_element = my_list[0]
print(first_element)  # Output: True

# Get the last element
last_element = my_list[-1]
print(last_element)  # Output: 6

# Get a sublist from index 2 to 5 (exclusive)
sublist = my_list[2:5]
print(sublist)  # Output: ['cherry', 'banana', 3]

# Get every other element
every_other_element = my_list[::2]
print(every_other_element)  # Output: [True, 'cherry', 3, 5]

# Reverse the list
reversed_list = my_list[::-1]
print(reversed_list)  # Output:
# [6, 5, 4, 1, 3, 'banana', 'cherry', 'orange', True]

# List concatenation:
# You can combine lists using the + operator.

# Example:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)  # Output: [1, 2, 3, 4, 5, 6]

# List multiplication:
# You can repeat a list multiple times using the * operator.

# Example:
repeated_list = [1, 2, 3] * 2
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3]



