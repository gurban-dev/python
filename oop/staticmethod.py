'''
The @staticmethod groups related behaviour together.

By putting utility functions like add() and subtract()
inside a class using @staticmethod, we avoid polluting
the global namespace and keep related functionality
organised in one place.

A utility function is one that is designed to perform
a particular task that is omnipresently needed across
different parts of a program.

E.g. len(), type(), print()

Global namespace pollution refers to the practice of
placing too many variables, functions, or classes in
the global (top-level) scope of a module or program.'''
class MathUtils:
  # Utility functions.

  # @staticmethod it indicates that a method belongs
  # to a class, but it does not access:
  # - self (represents an instance of the class)
  # - cls (represents the class itself)
  @staticmethod
  def add(num1, num2):
    return num1 + num2

  @staticmethod
  def subtract(num1, num2):
    return num1 - num2

print('MathUtils.add(10, 10):', MathUtils.add(10, 10))

# Instantiating the MathUtils class in spite of the
# fact that it doesn't have a constructor method.

# If you do not explicitly define an __init__ method
# (which serves as the constructor in Python) for a
# class, Python will automatically provide a default
# constructor.
math = MathUtils()

print('\nmath.subtract(100, 10):', math.subtract(100, 10))