'''
A class is a blueprint that defines what data an object
has and what functions (methods) can operate on that
data.

An object is a specific instance of a class that contains
its own data and can use the methods defined by the class.

The state of an object is defined with instance variables
and class variables.

The behaviour of an object is defined with methods.

Although not required, it is conventional practice
to make the file name match the class name.

File name (snake case):
coffee_machine.py

Class name (pascal case):
CoffeeMachine

Keep two empty lines above each class definition.
'''

# All Python classes implicitly inherit from the built-in base
# class named object.
class Coffee(object):
	'''
	The constructor initialises the state of an object
	when it is created.

	It runs automatically every time a new instance of
	the Coffee class is created.

	Every instance method must accept "self" as the
	first parameter.

	Methods with two leading and trailing underscores
	are called dunder methods in Python.
	'''
	def __init__(self, bean_type):

		'''
		Instance variable.

		Using "self." indicates that this variable
		belongs to the object.
		'''
		self.bean_type = bean_type

		print('\nCoffee class\' __init__() method invoked.')
		print('\nself.bean_type:', self.bean_type, '\n')


	'''
	A getter (selector) returns the value of an
	instance variable belonging to an object.
	'''
	def get_bean_type(self):
		return self.bean_type


	'''
	A setter (mutator) changes the value of an
	instance variable belonging to an object.
	'''
	def set_bean_type(self, bean_type):
		self.bean_type = bean_type
		print(f'\nself.bean_type updated to {bean_type}.\n')

	'''
	The __repr__() method returns an unambiguous
	string representation of the object.

	It is mainly intended for developers and debugging.
	'''
	def __repr__(self):
		return f"Coffee(bean_type='{self.bean_type}')"

	'''
	The __str__() method returns a readable string
	representation of the object.

	It is intended for end users.
	'''
	def __str__(self):
		return f"Coffee made from {self.bean_type} beans"


'''
Create an instance/object of the Coffee class.

The constructor requires an argument because it
expects the parameter "bean_type".
'''

# List of bean types.
bean_types = [
	'Arabica',
	'Robusta',
	'Liberica'
]

print("Bean Types:")

# Iterate through all elements in the list.
for bean_type in bean_types:
	print(bean_type)

# Accept input from the user.
bean_type = input(
  '\nEnter the bean type of your preference\n'
  'from the above menu: '
)

# Create an object of the Coffee class.
espresso = Coffee(bean_type)

# Call the getter method.
print('espresso.get_bean_type():', espresso.get_bean_type())

# Call the setter method.
espresso.set_bean_type('Robusta')

print('espresso.get_bean_type():', espresso.get_bean_type())

print('\nespresso:\n', espresso, sep="")
print('\nrepr(espresso):\n', repr(espresso), sep="")