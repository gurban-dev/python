'''
Polymorphism allows subclasses to have
methods with the same names as methods
in their superclasses. It gives the
ability for a program to call the correct
method depending on the type of object
that is used to call it.

Polymorphism is the ability of an object
to take many forms.

Two empty lines should be reserved above a
class definition.

The Mammal class represents a generic mammal.
The Mammal class is a superclass.'''
class Mammal:
  '''
  The __init__ method accepts an argument for
  the mammal's species. It is known as the
  constructor of a class and its purpose is to
  initialise the state of an object.'''
  def __init__(self, species):
    # Assign the parameter "species" to
    # instance variable called "__species".
    self.__species = species

    print('self.__species:', self.__species)

  # The show_species method displays a message
  # indicating the mammal's species.
  def show_species(self):
    print('I am a', self.__species)

  # The make_sound method is the mammal's
  # way of making a generic sound.
  def make_sound(self):
    print('Grrrrr\n')


# The Dog class is a subclass of the Mammal class.
class Dog(Mammal):
  '''
  The __init__ method calls the superclass's
  __init__ method passing 'Dog' as the species.

  Besides the "self" parameter, the __init__
  method doesn't accept any other parameters.'''
  def __init__(self):
    Mammal.__init__(self, 'Dog')

  # The make_sound method overrides the
  # superclass's make_sound method.
  def make_sound(self):
    print('Woof! Woof!\n')


# The Cat class is a subclass of the Mammal class.
class Cat(Mammal):
  # The __init__ method calls the superclass's
  # __init__ method passing 'Cat' as the species.
  def __init__(self):
    Mammal.__init__(self, 'Cat')

  # The make_sound method overrides the
  # superclass's make_sound method.
  def make_sound(self):
    print('Meow\n')