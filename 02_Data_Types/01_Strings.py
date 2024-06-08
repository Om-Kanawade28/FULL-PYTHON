
# Strings are immutable sequences of characters. They are enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''').


# Methods:
# - len(): Returns the length of the string.
# - upper(): Returns a copy of the string in uppercase.
# - lower(): Returns a copy of the string in lowercase.
# - strip(): Removes leading and trailing whitespace.
# - find(): Returns the index of the first occurrence of a substring.
# - replace(): Replaces all occurrences of a substring with another substring.
# - split(): Splits the string into a list of substrings based on a delimiter.
# - join(): Joins a list of strings into a single string using a delimiter.
# - format(): Formats a string using placeholders.

# Examples:
# Create a string
my_string = "Hello, world!"

# Get the length of the string
length = len(my_string)
print(length)  # Output: 13

# Convert to uppercase
uppercase_string = my_string.upper()
print(uppercase_string)  # Output: HELLO, WORLD!

# Convert to lowercase
lowercase_string = my_string.lower()
print(lowercase_string)  # Output: hello, world!

# Remove leading and trailing whitespace
stripped_string = "  Hello, world!  ".strip()
print(stripped_string)  # Output: Hello, world!

# Find the index of a substring
index = my_string.find("world")
print(index)  # Output: 7

# Replace a substring
replaced_string = my_string.replace("world", "Python")
print(replaced_string)  # Output: Hello, Python!

# Split the string into a list
words = my_string.split(",")
print(words)  # Output: ['Hello', ' world!']

# Join a list of strings into a single string
joined_string = " ".join(["Hello", "world"])
print(joined_string)  # Output: Hello world

# Format a string
name = "John"
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is John and I am 30 years old.

# String slicing:
# You can access individual characters or substrings of a string using slicing.
# Syntax: string[start:end:step]

# Examples:
# Get the first character
first_char = my_string[0]
print(first_char)  # Output: H

# Get the last character
last_char = my_string[-1]
print(last_char)  # Output: !

# Get a substring from index 2 to 5 (exclusive)
substring = my_string[2:5]
print(substring)  # Output: llo

# Get every other character
every_other_char = my_string[::2]
print(every_other_char)  # Output: Hlo,wr!

# Reverse the string
reversed_string = my_string[::-1]
print(reversed_string)  # Output: !dlrow ,olleH

# String concatenation:
# You can combine strings using the + operator.

# Example:
greeting = "Hello"
name = "John"
message = greeting + ", " + name + "!"
print(message)  # Output: Hello, John!

# String multiplication:
# You can repeat a string multiple times using the * operator.

# Example:
repeated_string = "Hello" * 3
print(repeated_string)  # Output: HelloHelloHello

# Note:
# - Strings are an essential data type in Python.
# - They are used for representing text and performing various text-related operations.
# - Understanding string methods and properties is crucial for working with text data.
# - Strings are immutable, so any modification creates a new string.
# - Slicing and concatenation are powerful techniques for manipulating strings.
