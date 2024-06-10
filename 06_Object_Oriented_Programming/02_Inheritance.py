# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows you to create new classes (derived classes) based on existing classes (base classes). This promotes code reusability and helps organize your code into a hierarchical structure.

# Key Concepts:

# - **Base Class (Parent Class):** The class from which other classes inherit.
# - **Derived Class (Child Class):** The class that inherits from the base class.
# - **Inheritance:** The process of creating a new class based on an existing class.
# - **Super Class:** Another name for the base class.
# - **Sub Class:** Another name for the derived class.

# Benefits of Inheritance:

# - **Code Reusability:**  Derived classes inherit attributes and methods from the base class, reducing code duplication.
# - **Code Organization:**  Inheritance helps organize code into a hierarchical structure, making it easier to understand and maintain.
# - **Extensibility:**  Derived classes can extend the functionality of the base class by adding new attributes and methods.
# - **Polymorphism:**  Inheritance supports polymorphism, allowing objects of different classes to be treated in a uniform way.

# Example:

# Let's create a base class called `Animal` and a derived class called `Dog`:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# Creating objects:

animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Calling the `speak` method:

animal.speak()  # Output: Generic animal sound
dog.speak()  # Output: Woof!

# Explanation:

# - The `Dog` class inherits from the `Animal` class.
# - The `Dog` class overrides the `speak` method from the `Animal` class, providing its own specific implementation.
# - When we call `speak` on the `animal` object, the `Animal` class's `speak` method is called.
# - When we call `speak` on the `dog` object, the `Dog` class's `speak` method is called, demonstrating polymorphism.

# Types of Inheritance with their proper example with explanition# Types of Inheritance:

# 1. Single Inheritance:

# A derived class inherits from a single base class.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        print("Woof!")

# 2. Multiple Inheritance:

# A derived class inherits from multiple base classes.

class Animal:
    def __init__(self, name):
        self.name = name

class Mammal:
    def __init__(self, fur_color):
        self.fur_color = fur_color

class Dog(Animal, Mammal):
    def speak(self):
        print("Woof!")

# 3. Multilevel Inheritance:

# A derived class inherits from another derived class, which in turn inherits from a base class.

class Animal:
    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

class Dog(Mammal):
    def speak(self):
        print("Woof!")

# 4. Hierarchical Inheritance:

# Multiple derived classes inherit from a single base class.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# 5. Hybrid Inheritance:

# A combination of multiple inheritance and hierarchical inheritance.

class Animal:
    def __init__(self, name):
        self.name = name

class Mammal:
    def __init__(self, fur_color):
        self.fur_color = fur_color

class Dog(Mammal, Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):# 6. Hybrid Inheritance:

# A combination of multiple inheritance and hierarchical inheritance.

class Animal:
    def __init__(self, name):
        self.name = name

class Mammal:
    def __init__(self, fur_color):
        self.fur_color = fur_color

class Dog(Mammal, Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Key Points:

# - Inheritance is a powerful tool for code reusability and organization.
# - Choose the appropriate type of inheritance based on your specific needs.
# - Use inheritance to create a hierarchy of classes that reflects real-world relationships.
# - Be mindful of the potential for complexity when using multiple inheritance.

