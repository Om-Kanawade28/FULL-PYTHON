

# Exception Handling in Python:

# Exception handling is a crucial aspect of robust programming. It allows you to gracefully handle unexpected errors or exceptions that may occur during program execution, preventing your program from crashing and ensuring a smoother user experience.

# 1. Basic Exception Handling:

#   - The `try...except` block is the fundamental mechanism for handling exceptions in Python.

#   - The `try` block encloses the code that might raise an exception.

#   - The `except` block catches and handles the exception if it occurs.

#   - Example:

try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Handle the ZeroDivisionError exception
    print("Error: Division by zero!")
#output:-
# Error: Division by zero!

# 2. Handling Multiple Exceptions:

#   - You can use multiple `except` blocks to handle different types of exceptions.

#   - Example:

try:
    # Code that might raise multiple exceptions
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
#output:-
# Enter a number: zero
# Error: Invalid input. Please enter a number.

# 3. The `else` Block:

#   - The `else` block is executed if no exception occurs within the `try` block.

#   - Example:

try:
    # Code that might raise an exception
    number = int(input("Enter a number: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Invalid input. Please enter a number.")
else:
    # Code to execute if no exception occurs
    print(f"Result: {result}")
#output:-
# Enter a number: 2
# Result: 5.0

# 4. The `finally` Block:

#   - The `finally` block is executed regardless of whether an exception occurs or not.

#   - It's often used for cleanup tasks, like closing files or releasing resources.

#   - Example

try:
    # Code that might raise an exception
    file = open("myfile.txt", "r")
    # ... process the file ...
except FileNotFoundError:
    print("Error: File not found!")
finally:
    # Close the file regardless of whether an exception occurred
    file.close()
#output:-
# Error: File not found!

# 5. Raising Exceptions:

#   - You can use the `raise` keyword to manually raise an exception.

#   - Example:

def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    else:
        return x / y

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Error: {e}")
#output:-
# Error: Cannot divide by zero!

# 6. Custom Exceptions:

#   - You can create your own custom exception classes by inheriting from the `Exception` class.

#   - Example:

class MyCustomError(Exception):
    pass

def check_input(value):
    if value < 0:
        raise MyCustomError("Input value must be non-negative.")

try:
    check_input(-5)
except MyCustomError as e:
    print(f"Error: {e}")
#output:-
# Error: Input value must be non-negative.

# 7. Exception Chaining:

#   - You can chain exceptions to provide more context about the error.

#   - Example:

try:
    # Code that might raise an exception
    file = open("myfile.txt", "r")
    # ... process the file ...
except FileNotFoundError as e:
    # Raise a new exception with the original exception as the cause
    raise IOError("Error reading file") from e
#output:-
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#   File "<stdin>", line 4, in open_file
# FileNotFoundError: [Errno 2] No such file or directory: 'myfile.txt'

# During exception handling, it's important to:

#   - Catch specific exceptions to handle them appropriately.
#   -
#   - Provide informative error messages to help with debugging.
#   - Use `finally` blocks for cleanup tasks.
#   - Consider creating custom exceptions for specific error conditions.

# Exception handling is a fundamental aspect of writing robust and reliable Python code. By handling exceptions effectively, you can create programs that are more resilient to errors and provide a better user experience.
