# Encapsulation is a fundamental principle in object-oriented programming (OOP) that involves bundling data (attributes) and methods (functions) that operate on that data within a single unit, known as a class. This encapsulation hides the internal implementation details of an object from the outside world, exposing only a controlled interface for interaction.

# Key Concepts:

# - **Data Hiding:**  Encapsulation restricts direct access to an object's internal data members. This is achieved through access modifiers (e.g., private, protected, public) that control visibility.
# - **Data Protection:**  Encapsulation helps protect data from accidental or malicious modification.
# - **Abstraction:**  Encapsulation supports abstraction by providing a simplified interface for interacting with an object, hiding complex internal details.
# - **Modularity:**  Encapsulation promotes modularity by encapsulating related data and methods within a class, making code easier to organize and maintain.

# Benefits of Encapsulation:

# - **Data Security:**  Encapsulation protects data from unauthorized access and modification, enhancing data integrity.
# - **Code Reusability:**  Encapsulated classes can be reused in different parts of a program or in other programs.
# - **Maintainability:**  Encapsulation makes code easier to maintain and debug by isolating changes within a class.
# - **Flexibility:**  Encapsulation allows for changes to the internal implementation of a class without affecting external code that uses it.

# Example:

# Let's create a class called `BankAccount` to represent a bank account:

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

# Creating an object:

account = BankAccount(1000)

# Accessing methods:

account.deposit(500)  # Output: Deposited 500. New balance: 1500
account.withdraw(200)  # Output: Withdrew 200. New balance: 1300
print(account.get_balance())  # Output: 1300

# Attempting to access the private attribute directly:

# print(account.__balance)  # This will raise an AttributeError

# Explanation:

# - The `__balance` attribute is declared as private using the double underscore (`__`) prefix.
# - This makes the attribute inaccessible from outside the class.
# - We can only access or modify the balance through the provided methods (`deposit`, `withdraw`, `get_balance`).
# - This ensures that the balance is updated and accessed in a controlled manner, maintaining data integrity.

# Encapsulation is a crucial concept in OOP that promotes data security, code organization, and maintainability. By encapsulating data and methods within classes, you can create robust and well-structured software systems.
#
#