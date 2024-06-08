
# Comments are used to explain code and make it more readable.
# They are ignored by the Python interpreter.
# Single-line comments start with a hash symbol (#).
# Multi-line comments are enclosed in triple quotes (''' ''' or """ """).

# Example:
# Single-line comment
# This is a single-line comment.

# Multi-line comment
'''
This is a multi-line comment.
It can span multiple lines.
'''

# Documentation Strings (Docstrings):
# Docstrings are multi-line strings used to document functions, classes, modules, and methods.
# They are written within triple quotes and are used by tools like help() and __doc__.

# Example:
def add(x, y):
    """
    This function adds two numbers.

    Args:
        x: The first number.
        y: The second number.

    Returns:
        The sum of x and y.
    """
    return x + y

# Print the docstring of the add function
print(add.__doc__)

# Output:
# This function adds two numbers.
#
# Args:
#     x: The first number.
#     y: The second number.
#
# Returns:
#     The sum of x and y.

# Best Practices for Comments and Documentation:
# - Use comments to explain complex logic or non-obvious code.
# - Keep comments concise and to the point.
# - Update comments when code changes.
# - Use docstrings to document functions, classes, modules, and methods.
# - Follow a consistent style for comments and docstrings.

# Example:
# A function that calculates the factorial of a number
def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n: The non-negative integer.

    Returns:
        The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Print the factorial of 5
print(factorial(5))

# Output:
# 120

# Example:
# A class that represents a bank account
class BankAccount:
    """
    Represents a bank account with a balance and deposit/withdraw methods.

    Attributes:
        balance: The current balance of the account.
    """

    def __init__(self, balance=0):
        """
        Initializes a new BankAccount object.

        Args:
            balance: The initial balance of the account.
        """
        self.balance = balance

    def deposit(self, amount):
        """
        Deposits money into the account.

        Args:
            amount: The amount to deposit.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraws money from the account.

        Args:
            amount: The amount to withdraw.

        Raises:
            ValueError: If the amount is greater than the balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

# Create a new bank account with an initial balance of 100
account = BankAccount(100)

# Deposit 50 into the account
account.deposit(50)

# Withdraw 25 from the account
account.withdraw(25)

# Print the current balance
print(account.balance)

# Output:
# 125

# Note:
# - Comments and documentation are essential for making code more readable and maintainable.
# - Docstrings are a standard way to document Python code.
# - Use comments and docstrings effectively to improve the quality of your code.
# - Use tools like help() and __doc__ to access docstrings.

