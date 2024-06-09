# Function Arguments in Python:

# Arguments are the values that you pass to a function when you call it. They provide input to the function, allowing it to perform its task with different data.

# 1. Positional Arguments:

#   - Positional arguments are passed to a function in the order they are defined.
#   - The order of arguments in the function call must match the order of parameters in the function definition.

#   - Example:

def greet(name, age):
    """Greets the user with a personalized message."""
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)  # Positional arguments
#output:-
# Hello, Alice! You are 30 years old.

# 2. Keyword Arguments:

#   - Keyword arguments are passed to a function using the parameter name followed by an equal sign (=) and the value.
#   - Keyword arguments allow you to pass arguments in any order, as the function will match them based on their names.

#   - Example:

def greet(name, age):
    """Greets the user with a personalized message."""
    print(f"Hello, {name}! You are {age} years old.")

greet(age=30, name="Alice")  # Keyword arguments
#output:-
# Hello, Alice! You are 30 years old.

# 3. Default Parameter Values:

#   - You can specify default values for parameters in a function definition.
#   - If a value is not provided for a parameter when the function is called, the default value is used.

#   - Example:

def greet(name, age=25):
    """Greets the user with a personalized message."""
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice")  # Uses the default age value
greet("Bob", 35)  # Overrides the default age value
#output:-
# Hello, Alice! You are 25 years old.
# Hello, Bob! You are 35 years old.

# 4. Arbitrary Number of Arguments:

#   - Use the `*args` syntax to allow a function to accept an arbitrary number of positional arguments.
#   - The `*args`
#     parameter will be a tuple containing all the positional arguments passed to the function.

#   - Example:

def sum_numbers(*numbers):
    """Calculates the sum of an arbitrary number of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total

result = sum_numbers(1, 2, 3, 4, 5)
print(f"Sum: {result}")
#output:-
# Sum: 15

# 5. Arbitrary Number of Keyword Arguments:

#   - Use the `**kwargs` syntax to allow a function to accept an arbitrary number of keyword arguments.
#   - The `**kwargs` parameter will be a dictionary containing all the keyword arguments passed to the function.

#   - Example:

def build_profile(first, last, **user_info):
    """Builds a dictionary containing a user's profile."""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("Albert", "Einstein", location="Princeton", field="Physics")
print(user_profile)
#output:-
# {'first_name': 'Albert', 'last_name': 'Einstein', 'location': 'Princeton', 'field': 'Physics'}

# 6. Passing a List as an Argument:

#   - You can pass a list as an argument to a function.
#   - The function can then access and modify the elements of the list.

#   - Example:

def print_list(items):
    """Prints each item in a list."""
    for item in items:
        print(item)

my_list = ["apple", "banana", "orange"]
print_list(my_list)
#output:-
# apple
# banana
# orange

# 7. Modifying a List in a Function:

#   - When you pass a list to a function, the function can modify the original list.
#   - This is because lists are mutable objects in Python.

#   - Example:

def add_item(items, new_item):
    """Adds a new item to a list."""
    items.append(new_item)

my_list = ["apple", "banana"]
add_item(my_list, "orange")
print(my_list)
#output:-
# ['apple', 'banana', 'orange']

# 8. Returning a Dictionary:

#   - Functions can return dictionaries.
#   - This allows you to create and return complex data structures from functions.

#   - Example:

def create_user(first_name, last_name):
    """Creates a dictionary representing a user."""
    user = {}
    user["first_name"] = first_name
    user["last_name"] = last_name
    return user

user = create_user("John", "Doe")
print(user)
#output:-
# {'first_name': 'John', 'last_name': 'Doe'}

# 9. Docstrings:

#   - Docstrings (documentation strings) are used to document your functions.
#   - They are enclosed in triple quotes (`"""Docstring goes here"""`).
#   - They are used by tools like help() and the interactive interpreter to provide information about your functions.

#   - Example:

def greet(name):
    """Greets the user with a personalized message."""
    print(f"Hello, {name}!")

help(greet)
#output:-
# Help on function greet in module __main__:
#
# greet(name)
#     Greets the user with a personalized message.

# Understanding function arguments is essential for writing flexible and reusable code in Python. By using different argument types, you can create functions that can handle various inputs and produce different outputs, making your code more adaptable and powerful.
#
#
#