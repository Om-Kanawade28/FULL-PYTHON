# Data types are the classification of data items that determine the values a variable can hold, the operations that can be performed on them, and the way they are stored in memory.

# Python has several built-in data types:

# 1. Numeric Types:
#     - Integers (int): Whole numbers without decimal points.
#         Example: 10, -5, 0
#     - Floating-point numbers (float): Numbers with decimal points.
#         Example: 3.14, -2.5, 1.0
#     - Complex numbers (complex): Numbers with real and imaginary parts.
#         Example: 2 + 3j, -1 - 2j

# 2. Boolean Type (bool):
#     - Represents truth values: True or False.
#         Example: True, False

# 3. Sequence Types:
#     - Strings (str): Ordered sequences of characters.
#         Example: "Hello", "Python", "123"
#     - Lists (list): Ordered sequences of elements of any data type.
#         Example: [1, 2, 3], ["apple", "banana", "cherry"], [True, False, True]
#     - Tuples (tuple): Ordered, immutable sequences of elements of any data type.
#         Example: (1, 2, 3), ("apple", "banana", "cherry"), (True, False, True)

# 4. Mapping Type:
#     - Dictionaries (dict): Unordered collections of key-value pairs.
#         Example: {"name": "John", "age": 30, "city": "New York"}

# 5. Set Types:
#     - Sets (set): Unordered collections of unique elements.
#         Example: {1, 2, 3}, {"apple", "banana", "cherry"}
#     - Frozen sets (frozenset): Immutable sets.
#         Example: frozenset({1, 2, 3}), frozenset({"apple", "banana", "cherry"})

# Example:
# Integer
age = 25
print(type(age))  # Output: <class 'int'>

# Float
price = 19.99
print(type(price))  # Output: <class 'float'>

# Complex
z = 2 + 3j
print(type(z))  # Output: <class 'complex'>

# Boolean
is_active = True
print(type(is_active))  # Output: <class 'bool'>

# String
name = "John Doe"
print(type(name))  # Output: <class 'str'>

# List
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>

# Tuple
coordinates = (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>

# Dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(type(person))  # Output: <class 'dict'>

# Set
numbers = {1, 2, 3}
print(type(numbers))  # Output: <class 'set'>

# Frozen set
letters = frozenset({"a", "b", "c"})
print(type(letters))  # Output: <class 'frozenset'>

# Data type conversion:
# You can convert data types using built-in functions like int(), float(), str(), bool(), list(), tuple(), set(), dict(), etc.

# Example:
# Convert a string to an integer
num_str = "10"
num_int = int(num_str)
print(type(num_int))  # Output: <class 'int'>

# Convert a float to a string
price = 19.99
price_str = str(price)
print(type(price_str))  # Output: <class 'str'>

# Convert a list to a tuple
fruits = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits)
print(type(fruits_tuple))  # Output: <class 'tuple'>

# Note:
# - Data types are fundamental to programming.
# - Understanding data types is crucial for writing correct and efficient code.
# - Python provides a variety of built-in data types to represent different kinds of data.
# - You can convert data types using built-in functions.
# - Choose the appropriate data type for your variables based on the type of data you are working with
# - Be aware of the limitations and characteristics of each data type.