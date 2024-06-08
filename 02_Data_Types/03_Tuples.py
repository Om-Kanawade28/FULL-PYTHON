# Tuples are immutable, ordered sequences of elements. They are enclosed in parentheses (()).
# Tuples can contain elements of different data types.

# Methods:
# - count(): Returns the number of occurrences of an element.
# - index(): Returns the index of the first occurrence of an element.

# Properties:
# - len(): Returns the length of the tuple.
# - min(): Returns the minimum element in the tuple.
# - max(): Returns the maximum element in the tuple.
# - sum(): Returns the sum of all elements in the tuple.

# Examples:
# Create a tuple
my_tuple = (1, 2, 3, "apple", "banana", True)

# Get the length of the tuple
length = len(my_tuple)
print(length)  # Output: 6

# Count the number of occurrences of "apple"
count = my_tuple.count("apple")
print(count)  # Output: 1

# Get the index of the first occurrence of "banana"
index = my_tuple.index("banana")
print(index)  # Output: 4

# Get the minimum element in the tuple
minimum = min(my_tuple)
print(minimum)  # Output: 1

# Get the maximum element in the tuple
maximum = max(my_tuple)
print(maximum)  # Output: True

# Get the sum of all elements in the tuple
total = sum(my_tuple)
print(total)  # Output: 6

# Tuple slicing:
# You can access individual elements or subtuples using slicing.
# Syntax: tuple[start:end:step]

# Examples:
# Get the first element
first_element = my_tuple[0]
print(first_element)  # Output: 1

# Get the last element
last_element = my_tuple[-1]
print(last_element)  # Output: True

# Get a subtuple from index 2 to 5 (exclusive)
subtuple = my_tuple[2:5]
print(subtuple)  # Output: (3, 'apple', 'banana')

# Get every other element
every_other_element = my_tuple[::2]
print(every_other_element)  # Output: (1
, 3, 'banana')

# Reverse the tuple
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)  # Output: (True, 'banana', 'apple', 3, 2, 1)

# Tuple concatenation:
# You can combine tuples using the + operator.

# Example:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Tuple multiplication:
# You can repeat a tuple multiple times using the * operator.

# Example:
repeated_tuple = (1, 2, 3) * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# Note:
# - Tuples are immutable, so you cannot modify their elements after creation.
# - Tuples are often used to represent fixed collections of data.
# - They are also used to return multiple values from a function.
# - Tuples are more efficient than lists for storing and accessing data.
# - They are also used as keys in dictionaries.
# - Tuples are a good choice when you need to ensure that data remains unchanged.
# - Tuples are often used in conjunction with lists and dictionaries.
# - They are a versatile data type that can be used in many different ways.

