from abc import ABC, abstractmethod

'''
Abstraction is the process of hiding complex implementation
details while exposing only the essential features of an
object.

Therefore, the focus can be on what the object does as
opposed to how it does it.

Key abstraction ideas:
You never instantiate BankAccount directly as it is an
abstract class.

You only know that each account must support deposit and withdraw.

How they actually do this is hidden (abstracted).
'''

# Abstract base class
class BankAccount(ABC):
  def __init__(self, balance):
    # Encapsulation:
    # _balance is a protected attribute.
    self._balance = balance

  # Abstract method forces subclasses to implement withdrawal rules.
  # withdraw() is merely an interface in this superclass.
  @abstractmethod
  def withdraw(self, amount):
    pass

  # Concrete method shared by all accounts
  def deposit(self, amount):
    self._balance += amount

  def get_balance(self):
    return self._balance


# A concrete subclass
class SavingsAccount(BankAccount):

  def withdraw(self, amount):
    if amount > self._balance:
      print("Insufficient funds!")
    else:
      self._balance -= amount


# Another concrete subclass
class CheckingAccount(BankAccount):

  def withdraw(self, amount):
    # Allows overdraft up to -50
    if self._balance - amount < -50:
      print("Overdraft limit exceeded!")
    else:
      self._balance -= amount

accounts = [
  SavingsAccount(100),
  CheckingAccount(100)
]

# Polymorphism in action since the withdraw() method
# takes more than one form.
for acc in accounts:
  acc.withdraw(120)
  print(acc.get_balance())
