'''
Programmers commonly organise their class definitions by
storing them in their own separate modules.

Then the modules can be imported into any programs that
need to use the classes they contain.'''
# import coin
from coin import Coin

# "c" is an alias for the Coin class
# defined in the coin.py module.
# from coin import Coin as c

def main():
	'''
	Create an object from the Coin class that was
	defined in coin.py.

	my_coin is the variable that references the object being
	generated.

	Notice that to qualify the name of the Coin class, the name
	of the module was prefixed followed by a dot.'''
	# my_coin = coin.Coin()

	# Object created with alias "c".
	# my_coin = c()

	my_coin = Coin()

	# Display the side of the coin that is facing up.
	print('This side is up:', my_coin.get_sideup())

	# Toss the coin.
	print('\nI am tossing the coin ...\n')

	my_coin.toss()

	# Legal, but an improper way to access instance variables.
	# print("my_coin.toss_count:", my_coin.toss_count)

	print("my_coin.get_toss_count():", my_coin.get_toss_count())

	print('\nThis side is up:', my_coin.get_sideup())

	# The following works, but should never be done in real code.
	# Always use getter and setter methods instead.

	# Name-mangling occurs with an instance variable that is private by
	# convention.

	# This means to directly access self.__sideup, my_coin._Coin__sideup
	# must be invoked instead of my_coin.__sideup.
	# my_coin._Coin__sideup = ''

	# Directly accessing the '__sideup' instance variable shows
	# that Python does not enforce strict private access like some
	# languages, but has name mangling (__var) to discourage external
	# access.
	print('\nmy_coin._Coin__sideup:', my_coin._Coin__sideup)

	# The get_sideup() method will return the same result.
	print('\nThis side is up:', my_coin.get_sideup())

# Prevents the main() function from being run automatically if
# this file is imported.
if __name__ == "__main__":
	main()