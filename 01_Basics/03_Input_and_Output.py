

# Input and Output in Python

# Input:
# - Getting data from the user or external sources.
# - The `input()` function is used to get input from the user.
# - The input is always returned as a string.

# Example:
name = input("Enter your name: ")
print("Hello,", name)

# Output:
# Enter your name: John Doe
# Hello, John Doe

# Output:
# - Displaying data to the user or external sources.
# - The `print()` function is used to display output.
# - You can print multiple values by separating them with commas.

# Example:
print("Hello, world!")
print("This is a message.")
print("1", "2", "3")

# Output:
# Hello, world!
# This is a message.
# 1 2 3

# Formatting Output:
# - You can format output using f-strings, which allow you to embed variables and expressions directly into strings.

# Example:
name = "John Doe"
age = 25
print(f"My name is {name} and I am {age} years old.")

# Output:
# My name is John Doe and I am 25 years old.

# Input and Output with Files:
# - You can read and write data to files using the `open()` function.

# Example:
# Write to a file
with open("my_file.txt", "w") as file:
    file.write("This is some text.")

# Read from a file
with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

# Output:
# This is some text.

# Note:
# - The `input()` function pauses the program execution and waits for the user to enter input.
# - The `print()` function displays output to the console.
# - F-strings provide a convenient way to format output.
# - Files can be opened in different modes:
#     - "w" for writing (overwrites existing files or creates new ones)
#     - "r" for reading
#     - "a" for appending (adds data to the end of existing files)
# - The `with` statement ensures that the file is
#   automatically closed after use.

# Example:
# Get user input for a number and print its square
number = int(input("Enter a number: "))
square = number * number
print(f"The square of {number} is {square}.")

# Output:
# Enter a number: 5
# The square of 5 is 25.

# Example:
# Read a file and print its contents line by line
with open("my_file.txt", "r") as file:
    for line in file:
        print(line, end="")

# Output:
# This is some text.

# Example:
# Write a list of names to a file
names = ["John", "Jane", "Peter"]
with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

# Example:
# Read a file and print the number of lines
with open("my_file.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

# Output:
# Number of lines: 1

# Example:
# Read a file and print the number of words
with open("my_file.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Number of words:", len(words))

# Output:
# Number of words: 4

# Example:
# Read a file and print the number of characters
with open("my_file.txt", "r") as file:
    content = file.read()
    print("Number of characters:", len(content))

# Output:
# Number of characters: 17

# Example:
# Read a file and print the first line
with open("my_file.txt", "r") as file:
    first_line = file.readline()
    print("First line:", first_line, end="")

# Output:
# First line: This is some text.

# Example:
# Read a file and print the last line
with open("my_file.txt", "r") as file:
    lines = file.readlines()
    last_line = lines[-1]
    print("Last line:", last_line, end="")

# Output:
# Last line: This is some text.