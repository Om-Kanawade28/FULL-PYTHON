

# Conditional statements are used to control the flow of execution in a program based on certain conditions. They allow you to make decisions and execute different blocks of code depending on whether a condition is true or false.

# Here's a breakdown of conditional statements in Python:

# 1. `if` Statement:
#   - The `if` statement is the most basic conditional statement. It executes a block of code only if a specified condition is true.


age = 25
if age >= 18:
    print("You are an adult.")
#output:-
# You are an adult.

# 2. `else` Statement:
#   - The `else` statement is used in conjunction with an `if` statement. It provides an alternative block of code to execute if the `if` condition is false.


age = 15
if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult yet.")
#output:-
# You are not an adult yet.


# 3. `elif` Statement:
#   - The `elif` (short for "else if") statement allows you to check multiple conditions in sequence. It executes the block of code associated with the first `elif` condition that evaluates to true.


score = 85
if score >= 90:
    print("Excellent!")
elif score >= 80:
    print("Very good!")
elif score >= 70:
    print("Good!")
else:
    print("Needs improvement.")
#output:-
# Very good!


# 4. Nested `if` Statements:
#   - You can nest `if` statements within other `if` statements to create more complex decision-making structures.


temperature = 25
if temperature > 30:
    print("It's very hot!")
else:
    if temperature > 20:
        print("It's warm.")
    else:
        print("It's cool.")
#output:-
# It's warm.


# 5. Short-Circuit Evaluation:
#   - Python uses short-circuit evaluation for logical operators (`and`, `or`). This means that if the first part of a logical expression determines the outcome, the second part is not evaluated.



x = 10
y = 0
if x > 5 and y > 0:
    print("Both conditions are true.")
else:
    print("At least one condition is false.")
#output:-
# At least one condition is false.

# In this example, the `and` operator is used to check if both `x > 5` and `y > 0` are true. Since `y > 0` is false, the second part of the expression is not evaluated, and the `else` block is executed.


# 6. `if` Statement with Multiple Conditions:
#   - You can combine multiple conditions using logical operators (`and`, `or`, `not`) within an `if` statement.


age = 20
is_student = True
if age >= 18 and is_student:
    print("You are eligible for a student discount.")
#output:-

# 7. `if` Statement with `in` Operator:
#   - The `in` operator can be used to check if a value is present in a sequence (like a list, tuple, or string).


fruits = ["apple", "banana", "orange"]
if "banana" in fruits:
    print("Banana is in the list.")

#output:-
# 8. `if` Statement with `not in` Operator:
#   - The `not in` operator can be used to check if a value is not present in a sequence.


fruits = ["apple", "banana", "orange"]
if "grape" not in fruits:
    print("Grape is not in the list.")

#output:-
# 9. `if` Statement with `is` Operator:
#   - The `is` operator checks if two variables refer to the same object in memory.


a = 10
b = 10
if a is b:
    print("a and b refer to the same object.")

#output:-

# 10. `if` Statement with `is not` Operator:
#   - The `is not` operator checks if two variables do not refer to the same object in memory.


a = 10
b = 15
if a is not b:
    print("a and b do not refer to the same object.")
#output:-

# Remember that conditional statements are essential for creating dynamic and responsive programs. They allow you to control the flow of execution based on specific conditions, making your code more flexible and adaptable.
