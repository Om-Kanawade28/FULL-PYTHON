#give notes about Dictionaries and short information about its methods and propertics their examlple
# Dictionaries are unordered collections of key-value pairs. They are enclosed in curly braces ({ }).
# Keys must be unique and immutable (e.g., strings, numbers, tuples).
# Values can be of any data type.

# Methods:
# - get(): Returns the value associated with a key.
# - keys(): Returns a view object containing all keys.
# - values(): Returns a view object containing all values.
# - items(): Returns a view object containing all key-value pairs.
# - update(): Updates the dictionary with key-value pairs from another dictionary or iterable.
# - pop(): Removes and returns the value associated with a key.
# - popitem(): Removes and returns an arbitrary key-value pair.
# - clear(): Removes all key-value pairs from the dictionary.

# Properties:
# - len(): Returns the number of key-value pairs in the dictionary.

# Examples:
# Create a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Get the value associated with a key
name = my_dict.get("name")
print(name)  # Output: John

# Get all keys
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['name', 'age', 'city'])

# Get all values
values = my_dict.values()
print(values)  # Output: dict_values(['John', 30, 'New York'])

# Get all key-value pairs
items = my_dict.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Update the dictionary
my_dict.update({"occupation": "Software Engineer"})
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Software Engineer'}

# Remove a key-value pair
popped_value = my_dict.pop("age")
print(popped_value)  # Output: 30
print(my_dict)  # Output: {'name': 'John', 'city': 'New York', 'occupation': 'Software Engineer'}

# Remove and return an arbitrary
# key-value pair
popped_item = my_dict.popitem()
print(popped_item)  # Output: ('city', 'New York')
print(my_dict)  # Output: {'name': 'John', 'occupation': 'Software Engineer'}

# Clear the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Get the length of the dictionary
length = len(my_dict)
print(length)  # Output: 0

# Note:
# - Dictionaries are useful for storing and accessing data in key-value pairs.
# - They are efficient for looking up values based on keys.
# - Dictionaries are often used to represent structured data, such as user profiles or configuration settings.
# - They are a versatile data type that can be used in many different ways.
# - Dictionaries are unordered, so you cannot access elements by index.
# - Dictionaries are mutable, so you can add, remove, or modify key-value pairs.
# - Keys must be unique and immutable.
# - Values can be of any data type.
# - Dictionaries are a good choice when you need to store and retrieve data based on unique keys.
# - They are often used in conjunction with other data structures like lists and sets.
# - Dictionaries are a powerful tool for working with data in Python.
# - Dictionaries are a good choice when you need to represent structured data.
# - They are also useful for storing and retrieving data based on unique keys.
.