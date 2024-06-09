# Lambda Functions in Python:

# Lambda functions are small, anonymous functions in Python. They are defined using the `lambda` keyword and can have any number of arguments but can only have one expression.

# 1. Basic Lambda Function:

#   - Example:

square = lambda x: x * x
result = square(5)
print(f"The square of 5 is: {result}")
#output:-
# The square of 5 is: 25

# 2. Lambda Function with Multiple Arguments:

#   - Example:

add = lambda x, y: x + y
result = add(3, 4)
print(f"3 + 4 = {result}")
#output:-
# 3 + 4 = 7

# 3. Using Lambda Functions with `map()`:

#   - The `map()` function applies a function to each item in an iterable.

#   - Example:

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(f"Squared numbers: {squared_numbers}")
#output:-
# Squared numbers: [1, 4, 9, 16, 25]

# 4. Using Lambda Functions with `filter()`:

#   - The `filter()` function creates an iterator that yields only the items from an iterable for which a function returns True.

#   - Example:

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
#output:-
# Even numbers: [2, 4]

# 5. Using Lambda Functions with `reduce()`:

#   - The `reduce()` function applies a function to pairs of items in an iterable, reducing it to a single value.

#   - Example:

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")
#output:-
# Product: 120

# 6. Lambda Functions as Arguments

#   - You can pass lambda functions as arguments to other functions.

#   - Example:

def my_function(func, arg):
    return func(arg)

result = my_function(lambda x: x * 2, 5)
print(f"Result: {result}")
#output:-
# Result: 10

# 7. Advantages of Lambda Functions:

#   - Concise and readable: Lambda functions provide a compact way to define simple functions.
#   - Flexibility: They can be used as arguments to other functions or assigned to variables.
#   - Anonymous: They don't require a formal function definition, making them suitable for one-time use.

# 8. Limitations of Lambda Functions:

#   - Single expression: Lambda functions can only contain a single expression.
#   - Limited functionality: They cannot contain complex logic or multiple statements.

# Lambda functions are a powerful tool in Python for creating concise and reusable functions. They are particularly useful for functional programming techniques and can simplify your code in many situations.
#
#
#