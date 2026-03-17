'''
Suppose we are writing a program to simulate
the tossing of a coin. In the program, we
need to repeatedly toss the coin and each
time determine whether it landed heads up or
tails up. Taking an object-oriented approach,
we will write a class named Coin that can
perform the behaviours of the coin.'''

# Importing the random module is necessary
# because we use the randint() function to
# generate a random number.
import random

# The class definition begins where
# the "class" keyword appears.

# The class name is "Coin" and conventionally,
# class names start with an uppercase letter.

# It is also convention to precede a class
# definition by two spaces, but

# The Coin class simulates a coin that can
# be flipped.
class Coin:
  '''
  The __init__() method is usually the first method
  inside a class definition. This is the class
  constructor.

  The __init__() method initializes the "sideup" data
  attribute with 'Heads'.

  Immediately after an object is created in memory, the
  __init__() method executes, and the self parameter is
  automatically assigned the object that was just created.'''
  def __init__(self):
    # Public data member or attribute.
    # Instance variable meaning that it is
    # unique to each object.
    # self.sideup = 'Heads'

    '''
    One underscore (_) preceding the name of an
    instance variable makes the instance variable
    protected by convention.
    
    Two underscores (__) preceding the name of an
    instance variable makes the instance variable
    private by convention. They also trigger
    name-mangling, so __sideup internally becomes
    _Coin__sideup.

    The phrase "by convention" must be included
    because private and protected access modifiers
    do not exist and are not enforced in Python,
    but it's a widely accepted practice among
    developers.

    The protected and private by convention
    instance variables exist in Python
    because they signal to other developers
    that certain instance variables shouldn't
    be directly accessed outside of the class
    they are defined in.

    Likewise there is no "public" access modifier,
    but instance variables are public by default.
    
    "public" means that the instance variable can
    be accessed outside of the class.'''
    self.__sideup = 'Heads'

    '''
    Public instance variable by default, but not
    explicitly specified with a "public" access
    modifier as it doesn't exist in Python.

    Upon creating an object of this Coin class,
    the default value for the "toss_count" data
    member is zero.'''
    self.toss_count = 0

  '''
  A method is a function that "belongs to" an object
  or instance of a class.

  Python documentation:
  https://docs.python.org/3/tutorial/classes.html#instance-objects

  The get_sideup() method returns the value referenced
  by sideup.

  Methods defined in a class are sometimes called
  "member functions".

  Selector/getter method because it returns the value
  of a instance variable back to where it was invoked
  in the program.'''
  def get_sideup(self):
    return self.__sideup

  # Mutator/Setter because it changes the value of a
  # data member which alters the state of an object.
  def toss(self):
    # random.randint(0, 1) generates a random
    # integer in the range of 0 through 1.
    # Either 0 or 1.
    if random.randint(0, 1) == 0:
      self.__sideup = 'Heads'
    else:
      self.__sideup = 'Tails'

'''
The Coin class consists of three methods:
__init__()
toss()
get_sideup()

The "self" parameter is required in every method
of a class.

When a method executes, it must have a way of
knowing which object's data attributes it is
supposed to operate on. That's where the self
parameter comes in. When a method is called,
Python makes the self parameter reference the
specific object that the method is supposed to
operate on.'''