# Sets are unordered collections of unique elements. They are enclosed in curly braces ({ }).
# Sets are mutable, meaning you can add or remove elements.
# Sets cannot contain duplicate elements.

# Methods:
# - add(): Adds an element to the set.
# - remove(): Removes a specific element from the set.
# - discard(): Removes a specific element from the set if it exists.
# - pop(): Removes and returns an arbitrary element from the set.
# - clear(): Removes all elements from the set.
# - union(): Returns a new set containing all elements from both sets.
# - intersection(): Returns a new set containing only the common elements from both sets.
# - difference(): Returns a new set containing elements that are in the first set but not in the second set.
# - symmetric_difference(): Returns a new set containing elements that are in either the first or second set, but not both.
# - update(): Adds elements from another iterable to the set.
# - intersection_update(): Updates the set with the intersection of itself and another set.
# - difference_update(): Updates the set with the difference of itself and another set.
# - symmetric_difference_update(): Updates the set with the symmetric difference of itself and another set.
# - isdisjoint(): Returns True if the set has no elements in common with another set.
# - issubset(): Returns True if the set is a subset of another set.
# - issuperset(): Returns True if the set is a superset of another set.

# Properties:
# - len(): Returns the number of elements in the set.

# Examples:
# Create a set
my_set = {1, 2, 3, "apple", "banana"}

# Add an element
my_set.add("cherry")
print(my_set)  # Output: {1, 2, 3, 'apple', 'banana', 'cherry'}

# Remove an element
my_set.remove("banana")
print(my_set)  # Output: {1, 2, 3, 'apple', 'cherry'}

# Discard an element (if it exists)
my_set.discard("orange")
print(my_set)  # Output: {1, 2, 3, 'apple', 'cherry'}

# Remove and return
# an arbitrary element
popped_element = my_set.pop()
print(popped_element)  # Output: 1
print(my_set)  # Output: {2, 3, 'apple', 'cherry'}

# Clear the set
my_set.clear()
print(my_set)  # Output: set()

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Difference
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Update
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}

# Intersection update
set1.intersection_update(set2)
print(set1)  # Output: {3}

# Difference update
set1.difference_update(set2)
print(set1)  # Output: set()

# Symmetric difference update
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}

# Is disjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
is_disjoint = set1.isdisjoint(set2)
print(is_disjoint)  # Output: True

# Is subset
set1 = {1, 2}
set2 = {1, 2, 3}
is_subset = set1.issubset(set2)
print(is_subset)  # Output: True

# Is superset
set1 = {1, 2, 3}
set2 = {1, 2}
is_superset = set1.issuperset(set2)
print(is_superset)  # Output: True

# Get the length of the set
length = len(my_set)
print(length)  # Output: 0

# Note:
# - Sets are useful for storing unique elements and performing set operations.
# - They are efficient for checking membership and removing duplicates.
# - Sets are often used in conjunction with other data structures like lists and dictionaries.
# - They are a powerful tool for working with data in Python.
# - Sets are unordered, so you cannot access elements by index.
# - Sets are mutable, so you can add or remove elements.
# - Sets cannot contain duplicate elements.
# - Sets are a good choice when you need to ensure that data is unique.
# - Sets are often used in conjunction with other data structures like lists and dictionaries.
# - They are a versatile data type that can be used in many different ways.
# - Sets are a good choice when you need to perform set operations like union, intersection, difference, and symmetric difference.
# - Sets are also useful for checking membership and removing duplicates.
