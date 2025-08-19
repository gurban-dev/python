'''
A class is a blueprint for an object that will
have state and behaviour.

The state of an object is defined with instance
variables.

The behaviour of an object is defined with methods
that are defined within the class.

Unlike Java, the name of the Python file
isn't required to match the name of the
class declared inside of it.

Although not a strict requirement, it is
conventional practice to make the name of
a file the same as the class declared in
it, but written in snake case:

Class name (pascal naming convention):
CoffeeMachine

File name (snake case naming convention):
coffee_machine.py

Keep two empty lines above each class definition.'''
class Coffee:
  '''
  The following is the constructor of this class.

  The constructor of a class is responsible for
  initialising the state of an object upon its
  creation. This means that the constructor is
  invoked every time a new object/instance of
  the Coffee class is created.

  The constructor should always be the first function
  declared within a class.

  The constructor is also a method. Every method
  in a class must accept the "self" keyword as
  its first parameter.'''
  def __init__(self, bean_type):
    '''
    Instance variable/data member

    Prepending the "bean_type" with "self."
    makes it clear that the following is an
    instance variable.'''
    self.bean_type = bean_type

    print('\nCoffee class\' __init__ method invoked.')

    print('\nself.bean_type:', self.bean_type, '\n')

  '''
  Python does not support true method overloading
  for __init__ (or any method) in the way that
  programming languages like Java or C++ do. If you
  define multiple __init__ methods within a single
  class, only the last one defined will be used.'''

  '''
  The get_bean_type() function is a method.
  A method is a function that "belongs to" an object.

  The subsequent method is often called a "selector"
  or "getter" function because it returns an instance
  variable/data member that belongs to an object.'''

  # Getter/selector
  def get_bean_type(self):
    '''
    Notice that the "self" keyword must be
    included in order to reference the instance
    variable that is unique to this particular
    object/instance.'''
    return self.bean_type
  
  '''
  The ensuing method is often referred to as a setter
  /mutator because it changes the value of an instance
  variable/data member that belongs to an object.'''
  
  # Setter/mutator
  def set_bean_type(self, bean_type):
    self.bean_type = bean_type

    print(f'\nself.bean_type updated to {bean_type}.\n')

'''
Create an instance/object of the class Coffee.
You must use the same name of the class when
creating an object/instance of that class.

The name of the object, "espresso" in this case,
is less important.

An argument must be provided when invoking the
class name "Coffee" because in the class constructor,
you can see that there is a parameter called "bean_type".

The argument being passed to the constructor is
'arabica'.'''

bean_types = [
  'Arabica',
  'Robusta',
  'Liberica'
]

# The vertical way of creating a list
# data structure is more readable as
# visible above.
# bean_types = ['Arabica', 'Robusta', 'Liberica']

# Iterate through all of the elements
# in the "bean_types" list.
for bean_type in bean_types:
  print(bean_type)

# print(bean_types)

# Accept input from the end user.
bean_type = input(
  '\nEnter the bean type of your preference\n' \
  'from the above menu: '
)

espresso = Coffee(bean_type)

# espresso = Coffee('arabica')

print('espresso.get_bean_type():', espresso.get_bean_type())

espresso.set_bean_type('robusta')

print('espresso.get_bean_type():', espresso.get_bean_type())