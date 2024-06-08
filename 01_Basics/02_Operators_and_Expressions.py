

# Operators are special symbols that perform operations on values or variables.
# Expressions are combinations of operators, values, and variables that evaluate to a single value.

# Arithmetic Operators:
# + (Addition)
# - (Subtraction)
# * (Multiplication)
# / (Division)
# % (Modulo - Remainder of division)
# ** (Exponentiation)
# // (Floor division - Rounds down to the nearest integer)

# Example:
x = 10
y = 5
sum = x + y  # Addition
difference = x - y  # Subtraction
product = x * y  # Multiplication
quotient = x / y  # Division
remainder = x % y  # Modulo
power = x ** y  # Exponentiation
floor_division = x // y  # Floor division

# Comparison Operators:
# == (Equal to)
# != (Not equal to)
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)

#Example:
x = 10
y = 5
is_equal = x == y  # False
is_not_equal = x != y  # True
is_greater = x > y  # True
is_less = x < y  # False
is_greater_or_equal = x >= y  # True
is_less_or_equal = x <= y  # False

# Logical Operators:
# and (Logical AND)
# or (Logical OR)
# not (Logical NOT)

# Example:
# x = True
# y = False
# logical_and = x and y  # False
# logical_or = x or y  # True
# logical_not = not x  # False

# Assignment Operators:
# = (Assignment)
# += (Add and assign)
# -= (Subtract and assign)
# *= (Multiply and assign)
# /= (Divide and assign)
# %= (Modulo and assign)
# **= (Exponentiation and assign)
# //= (Floor division and assign)

# Example:
# x = 10
# x += 5  # x = x +
# x -= 5  # x = x - 5
# x *= 5  # x = x * 5
# x /= 5  # x = x / 5
# x %= 5  # x = x % 5
# x **= 5  # x = x ** 5
# x //= 5  # x = x // 5

# Bitwise Operators:
# & (Bitwise AND)
# | (Bitwise OR)
# ^ (Bitwise XOR)
# ~ (Bitwise NOT)
# << (Left shift)
# >> (Right shift)

# Example:
# x = 10  # Binary: 1010
# y = 5   # Binary: 0101
# bitwise_and = x & y  # Binary: 0000 (Decimal: 0)
# bitwise_or = x | y  # Binary: 1111 (Decimal: 15)
# bitwise_xor = x ^ y  # Binary: 1111 (Decimal: 15)
# bitwise_not = ~x  # Binary: 10101 (Decimal: -11)
# left_shift = x << 2  # Binary: 101000 (Decimal: 40)
# right_shift = x >> 2  # Binary: 0010 (Decimal: 2)

# Identity Operators:
# is (Identity)
# is not (Not identity)

# Example:
x = 10
y = 10
is_same = x is y  # True
is_not_same = x is not y  # False

# Membership Operators:
# in (Membership)
# not in (Not membership)

# Example:
fruits = ["apple", "banana", "orange"]
is_present = "apple" in fruits  # True
is_not_present = "grape" in fruits  # False

# Operator Precedence:
# Operators have a specific order of precedence, which determines the order in which they are evaluated in an expression.
# Parentheses () have the highest precedence.
# Exponentiation ** has the next highest precedence.
#
# Example:
x = 10
y = 5
z = 2
result = x + y * z  # Evaluates to 20 (y * z is evaluated first)
result = (x + y) * z  # Evaluates to 30 (x + y is evaluated first)

# Operator Associativity:
# Operators with the same precedence are evaluated from left to right, except for exponentiation, which is evaluated from right to left.

# Example:
x = 10
y = 5
z = 2
result = x / y * z  # Evaluates to 4 (x / y is evaluated first)
result = x ** y ** z  # Evaluates to 1000000 (y ** z is evaluated first)

# Note:
# - Operators are used to perform operations on values or variables.
# - Expressions are combinations of operators, values, and variables that evaluate to a single value.
# - Operator precedence and associativity determine the order in which operators are evaluated in an expression.
# - Understanding operators and expressions is essential for writing effective Python code.

# Example:
# Calculate the area of a rectangle
length = 10
width = 5
area = length * width
print("Area of the rectangle:", area)

# Output:
# Area of the rectangle: 50

# Example:
# Check if a number is even or odd
number = 15
is_even = number % 2 == 0
print("Is the number even?", is_even)

# Output:
# Is the number even? False

# Example:
# Calculate the average of three numbers
num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3) / 3
print("Average of the numbers:", average)

# Output:
# Average of the numbers: 20.0