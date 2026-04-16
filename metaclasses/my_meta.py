
# A metaclass defines the rules for how a class is created.

# Metaclasses exist to control the class creation process.

# In Python, a class is an instance of a metaclass.

# A metaclass is a blueprint for a class.
class MyClass:
	x = 5

# The metaclass of MyClass is type.
print('type(MyClass):', type(MyClass))

# Internally, Python uses the metaclass (type by default) to
# create the class object when the class statement is executed.
MyClass = type('MyClass', (), {'x': 5})

'''
type(name, bases, dct) creates a class dynamically.

name -> class name

bases -> tuple of parent classes

dct -> dictionary of attributes and methods


Class Creation Lifecycle in Python (Using a Metaclass)

Step 1 -> __prepare__() returns a namespace object (usually an empty dict)
Step 2 -> The class body executes and populates that namespace (e.g., x, y)
Step 3 -> The final namespace looks like {'x': 1, 'y': 2}
Step 4 -> __new__() is called to create the class object (not an instance
		  of the class)
Step 5 -> __init__() is called to finalise the class
'''

class MyMeta(type):
	# __new__() is a dunder method because it begins with
	# two underscores.

	# __new__() is invoked as soon as Python executes the class
	# statement, before any objects of that class exist.
	def __new__(cls, name, bases, dct):
		print(f'\nCreating class {name}')

		# dct (the class dictionary) can be modified to add
		# attributes or methods.

		# Give classes that use this metaclass a method named
		# greet.
		dct['greet'] = lambda self: print(f'\nHello from {name}.')

		print(f"Metaclass: {cls}\n"
			f"Class Name: {name}\n"
			f"Base Classes: {bases}\n"
			f"Class Dict: {dct}")

		# super().__new__() creates the class object.
		return super().__new__(cls, name, bases, dct)
	
	def __init__(cls, name, bases, dct):
        print(f"Initialising class {name}")

        super().__init__(name, bases, dct)
  
# Use the MyMeta metaclass.
class MyClass(metaclass=MyMeta):
	pass

my_class_obj = MyClass()

my_class_obj.greet()

"""
When would you use a meta class and why?

I'd use a metaclass when I need to control or enforce behavior
at class creation time rather than at instance level.

For example, in a portfolio analytics system, I could use a
metaclass to ensure every asset class defines methods like
valuation and risk calculation, and also automatically
register each asset class in a central registry.

An abstract base class can enforce that required methods are
implemented, but it does that at instantiation time and relies
on inheritance. It doesn't let you modify or control how the
class itself is created.

So if enforcement alone is enough, I'd use an abstract base class.
If I need automatic registration or to modify classes as they're
defined, I'd use a metaclass.

That said, I'd avoid metaclasses unless I really need that level
of control, since they add complexity and make code harder to
reason about. In most cases, abstract base classes or composition
are simpler and more maintainable.


Why not use ABC (abstract base classes)?

I would avoid metaclasses unless I truly need class-level control, because
they add complexity and reduce readability. In most cases, I'd prefer
abstract base classes or simple composition.
"""