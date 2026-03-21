'''
Suppose we are writing a program to simulate the tossing
of a coin. In the program, we need to repeatedly toss
the coin and each time determine whether it landed heads
up or tails up. Taking an object-oriented approach, we
will write a class named Coin that can perform the
behaviours of the coin.
'''

# Importing the random module because we use
# the randint() function to generate a random number.
import random

# The Coin class simulates a coin that can be flipped.
# Class names conventionally start with an uppercase letter.
class Coin:

	'''
	The __init__() method is the class constructor.

	It runs automatically when a new object is created
	and initialises the object's data attributes.
	'''
	def __init__(self):

		'''
		Two underscores (__) preceding the name of an instance
		variable signals that it should be treated as private
		by convention.

		Python does not strictly enforce private access,
		but this naming style tells other developers that
		the variable should not be accessed outside the class.

		Internally Python performs name-mangling, so
		__sideup becomes _Coin__sideup.
		'''
		self.__sideup = 'Heads'

		'''
		Treated as a public instance variable.

		Upon creating an object of this class,
		the default value of toss_count is zero.
		'''
		self.toss_count = 0

	'''
	A method is a function that belongs to an object.

	The get_sideup() method returns the value of
	the side currently facing up.
	'''
	def get_sideup(self):
		return self.__sideup
	
	def get_toss_count(self):
		return self.toss_count

	'''
	Mutator method because it changes the value
	of a data member.
	'''
	def toss(self):

		# random.randint(0 (inclusive), 1 (inclusive))
		# generates either 0 or 1.
		if random.randint(0, 1) == 0:
			self.__sideup = 'Heads'
		else:
			self.__sideup = 'Tails'
		
		self.toss_count += 1