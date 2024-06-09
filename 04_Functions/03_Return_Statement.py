# The `return` Statement in Python:

# The `return` statement is used to specify the value that a function should return to the caller. It is an essential part of function design, allowing you to pass data back from a function to the part of the code that called it.

# 1. Basic Return:

#   - The simplest form of `return` is to return a single value.

#   - Example:

def square(number):
    """Returns the square of a number."""
    return number * number

result = square(5)
print(f"The square of 5 is: {result}")
#output:-
# The square of 5 is: 25

# 2. Returning Multiple Values:

#   - You can return multiple values from a function using a tuple.

#   - Example:

def get_user_info():
    """Returns the user's name and age."""
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

name, age = get_user_info()
print(f"Name: {name}, Age: {age}")
#output:-
# Enter your name: Alice
# Enter your age: 30
# Name: Alice, Age: 30

# 3. Returning None:

#   - If a function does not have a `return` statement or if it reaches the end of the function without encountering a `return` statement, it implicitly returns `None`.

#   - Example:

def greet(name):
    """Greets the user with a personalized message."""
    print(f"Hello, {name}!")

result = greet("Alice")
print(f"Return value: {result}")
#output:-
# Hello, Alice!
# Return value: None

# 4. Using `return` to Exit a Function:

#   - You can use `return` to exit a function early, even if the function has not reached the end of its code.

#   - Example:

def check_password(password):
    """Checks if a password meets certain criteria."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

password = input("Enter your password: ")
if check_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")
#output:-
# Enter your password: Password123
# Password is valid.

# 5. Returning a List:

#   - Functions can return lists, allowing you to create and return collections of data.

#   - Example:

def get_even_numbers(numbers):
    """Returns a list of even numbers from a given list."""
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = get_even_numbers(numbers)
print(f"Even numbers: {even_numbers}")
#output:-
# Even numbers: [2, 4, 6]

# 6. Returning a Dictionary:

#   - Functions can return dictionaries, allowing you to create and return complex data structures.

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

# The `return` statement is a fundamental part of function design in Python. It allows you to pass data back from a function to the caller, enabling you to create modular and reusable code. By understanding how to use `return` effectively, you can write more efficient and organized Python programs.
