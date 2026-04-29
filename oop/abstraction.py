from abc import ABC, abstractmethod

'''
Abstraction is the process of hiding complex implementation
details while exposing only the essential features of an
object.

Therefore, the focus can be on what the object does as opposed
to how it does it.

Program summary:
The BankAccount class defines what every bank account should
be able to do (deposit, withdraw), but it doesn't define how
it does it.

An abstract base class (ABC) is a class that defines a template
for other classes, but it isn't meant to be used on its own.

Note that an abstract base class cannot be instantiated.
An object/instance of BankAccount cannot be created.

You only know that each account must support deposit and withdraw.

How they actually do this is hidden (abstracted).
'''

# BankAccount is an abstract base class because its inheriting
# from the ABC class.
class BankAccount(ABC):
	def __init__(self, balance):
		# Encapsulation:
		# The balance is kept hidden using a protected attribute
		# (_balance).

		# The outside world must use methods (deposit, withdraw,
		# get_balance) to interact with it.
		self._balance = balance

	# An abstract method forces subclasses to implement withdrawal
	# rules. The implementation details are hidden in the abstract
	# base class.

	# withdraw() is merely an interface in this superclass.
	@abstractmethod
	def withdraw(self, amount):
		# pass is a placeholder statement used when Python requires
		# a code block, but no action needs to be executed.
		pass

	# Mutator/setter
	def deposit(self, amount):
		self._balance += amount

	# Selector/getter
	def get_balance(self):
		return self._balance

# Inheritance:
# CheckingAccount and SavingsAccount inherit from BankAccount.
class CheckingAccount(BankAccount):
	def withdraw(self, amount):
		# Allows an overdraft up to 50.
		if self._balance - amount < -50:
			print("Overdraft limit exceeded!")
		else:
			# self._balance = self._balance - amount
			self._balance -= amount


class SavingsAccount(BankAccount):
	def withdraw(self, amount):
		if amount > self._balance:
			print("\nInsufficient funds!")
		else:
			# self._balance = self._balance - amount
			self._balance -= amount

accounts = [
	CheckingAccount(balance=100),
	SavingsAccount(balance=100)
]

# Polymorphism:
# Each subclass implements the withdraw() method differently,
# but account.withdraw() is invoked the same way.

# The withdraw() method takes more than one form.
for account in accounts:
	# Dunder variables/attributes:
	# __class__ reveals what data type (class) an object belongs to.

	# E.g.
	# num = 1
	# __name__ is the name of the class.

	# num.__class__ returns <class 'int'>.

	# num.__class__.__name__ return 'int'.

	print('account.__class__.__name__:', account.__class__.__name__)

	# Notice how for the SavingsAccount object, withdrawing
	# 120 in monetary currency cannot occur.
	account.withdraw(120)

	print('account.get_balance():', account.get_balance(), '\n')