from abc import ABC, abstractmethod

'''
Abstraction is the process of hiding complex implementation
details while exposing only the essential features of an
object.

Therefore, the focus can be on what the object does as
opposed to how it does it.

Program summary:
The BankAccount class defines what every bank account should
be able to do (deposit, withdraw), but it doesn't define how
it does it.

BankAccount is an abstract class so it cannot be instantiated.

You only know that each account must support deposit and withdraw.

How they actually do this is hidden (abstracted).
'''

# BankAccount is an abstract base class because its inheriting
# from ABC.
class BankAccount(ABC):
  def __init__(self, balance):
    # Encapsulation:
    # The balance is kept hidden using a protected attribute
    # (_balance).

    # The outside world must use methods (deposit, withdraw,
    # get_balance) to interact with it.
    self._balance = balance

  # An abstract method forces subclasses to implement withdrawal
  # rules.
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
    # Allows an overdraft up to -50.
    if self._balance - amount < -50:
      print("Overdraft limit exceeded!")
    else:
      # self._balance = self._balance - amount
      self._balance -= amount


class SavingsAccount(BankAccount):

  def withdraw(self, amount):
    if amount > self._balance:
      print("Insufficient funds!")
    else:
      # self._balance = self._balance - amount
      self._balance -= amount

accounts = [
  CheckingAccount(balance=100),
  SavingsAccount(balance=100)
]

# Polymorphism:
# Each subclass implements the withdraw() method differently,
# but acc.withdraw() is invoked the same way.

# The withdraw() method takes more than one form.
for acc in accounts:
  print('acc.__class__.__name__:', acc.__class__.__name__)

  # Notice how for the SavingsAccount object, withdrawing
  # 120 cannot occur.
  acc.withdraw(120)

  print('acc.get_balance():', acc.get_balance(), '\n')
