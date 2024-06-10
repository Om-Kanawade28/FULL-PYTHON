# add full information of Polymorphism with example
# Polymorphism is a core concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common type. This means that you can use the same interface (methods) to interact with objects of different classes, even though they might implement those methods differently.

# Key Concepts:

# - **Common Interface:**  Polymorphism relies on having a common interface, typically defined by a base class or an interface, that is shared by different derived classes.
# - **Method Overriding:**  Derived classes can override methods inherited from the base class, providing their own specific implementations.
# - **Dynamic Binding:**  The actual method that is called at runtime is determined based on the type of the object, not the type of the variable.

# Benefits of Polymorphism:

# - **Code Reusability:**  Polymorphism allows you to write code that can work with objects of different classes, promoting code reusability.
# - **Flexibility:**  Polymorphism makes your code more flexible and adaptable to changes, as you can easily add new classes that implement the common interface.
# - **Maintainability:**  Polymorphism simplifies code maintenance by reducing the need for conditional statements to handle different object types.
# - **Readability:**  Polymorphic code is often more readable and easier to understand, as it focuses on the common interface rather than specific implementations.

# Example:

# Let's create a base class called `Animal` and two derived classes, `Dog` and `Cat`:

class Animal:
    def speak(self):
        print("Generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

# Creating objects:

animal = Animal()
dog = Dog()
cat = Cat()

# Calling the `speak` method:

animal.speak()  # Output: Generic animal sound
dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!

# Explanation:

# - The `speak` method is defined in the `Animal` class and overridden in the `Dog` and `Cat` classes.
# - When we call `speak` on the `animal` object, the `Animal` class's `speak` method is called.
# - When we call `speak` on the `cat` object, the `Cat` class's `speak` method is called.

# Polymorphism in Action:

# We can use a list to store objects of different classes and call the `speak` method on each object:

animals = [animal, dog, cat]

for animal in animals:
    animal.speak()  # Output: Generic animal sound, Woof!, Meow!

# In this example, the `speak` method is called on each object in the list, regardless of its specific type. This is because the `speak` method is defined in the common interface (`Animal` class).

# Polymorphism is a powerful concept that enhances code reusability, flexibility, and maintainability. It allows you to write code that can work with objects of different classes in a unified way, making your programs more adaptable and easier to understand.
