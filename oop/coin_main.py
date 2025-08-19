'''
Programmers commonly organize their class
definitions by storing them in their own
separate modules.

Then the modules can be imported into any
programs that need to use the classes they
contain.'''
# import coin
from coin import Coin

# "c" is an alias for the Coin class
# defined in the coin.py module.
from coin import Coin as c

def main():
  '''
  Create an object from the Coin class that was
  defined in coin.py.

  my_coin is the name of the object being generated.
  my_coin is also called an instance of the Coin class.

  Notice that to qualify the name of the Coin class,
  the name of the module was prefixed followed by a
  dot.'''
  # my_coin = coin.Coin()

  # Object created with alias "c".
  # my_coin = c()

  my_coin = Coin()

  # Display the side of the coin that is facing up.
  print('This side is up:', my_coin.get_sideup())

  # Toss the coin.
  print('\nI am tossing the coin ...')
  my_coin.toss()

  print('\nThis side is up:', my_coin.get_sideup())

  '''
  The fact that the "sideup" instance variable is
  able to be mutated or modified outside of the
  Coin class, validates that private access modifiers
  do not exist in Python.'''

  # Name-mangling occurs with an instance
  # variable that is private by convention.

  # This mean to directly access self.__sideup,
  # my_coin._Coin__sideup must be invoked
  # instead of my_coin.sideup.
  my_coin._Coin__sideup = ''

  # Directly accessing the "sideup" instance
  # variable is a testimony to the lack of
  # the private access modifier in Python.
  print('\nmy_coin._Coin__sideup:', my_coin._Coin__sideup)

  # The get_sideup() method will return the same
  # result.
  print('\nThis side is up:', my_coin.get_sideup())

main()