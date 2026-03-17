# A metaclass defines the rules for how a class
# is created.

# In Python, a class is an instance of a metaclass.
# A metaclass is a blueprint for a class.
class MyClass:
  x = 5

# The metaclass of MyClass is type.
print('type(MyClass):', type(MyClass))

# Internally, Python executes the following instruction
# when an object of the above class is created.
MyClass = type('MyClass', (), {'x': 5})

'''
type(name, bases, dict) creates a class dynamically

name → class name

bases → tuple of parent classes

dict → dictionary of attributes and methods
'''

class MyMeta(type):
  # __new__() is a dunder method because it begins with
  # two underscores.

  # __new__() is invoked as soon as Python executes the class
  # statement, before any objects of that class exist.
  def __new__(cls, name, bases, dict):
    print(f'\nCreating class {name}')

    # dct (the class dictionary) can be modified to add
    # attributes or methods.

    # Give classes that use this metaclass a method named
    # greet.
    dict['greet'] = lambda self: print(f'\nHello from {name}.')

    print(f"Metaclass: {cls}\n"
          f"Class Name: {name}\n"
          f"Base Classes: {bases}\n"
          f"Class Dict: {dict}")

    # super().__new__() creates the class object.
    return super().__new__(cls, name, bases, dict)
  
# Use the MyMeta metaclass.
class MyClass(metaclass=MyMeta):
  pass

my_class_obj = MyClass()

my_class_obj.greet()