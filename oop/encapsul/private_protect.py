
# Parent class

# By default, all classes in Python inherit from a class named
# 'type'.
class BankAccount:
    def __init__(self):
        # A single underscore signals, don't directly access this
        # outside of the class, but it doesn't internally alter
        # the name of the instance variable the way two underscores
        # would.

        # Although doesn't have a strict access modifier named protectd
        # the same way that Java does, a single underscore is "protected"
        # by naming convention.
        self._balance = 1_000

    def get_balance(self):
        return self._balance

# Child class
class SavingsAccount(BankAccount):
    def __init__(self):
        # Call the parent class' constructor method.
        # super().__init__()

        BankAccount.__init__(self)

        # Unintentionally overwriting the parent's instance variable.
        # self._balance = 0

        # Create a new instance variable instead of overwriting the
        # parent's.
        self.__balance = 0

        # The two underscores that precede "balance" force the instance
        # to become the following internally:
        # self._SavingsAccount__balance = 0

savings_acc = SavingsAccount()

# The instance variable self._balance can still be accessed
# directly from outside the class.
# savings_acc._balance -= 1_000

# Output is 1000 because __balance in the child class does not
# overwrite _balance in the parent class. They are different
# variables.
print("savings_acc.get_balance():", savings_acc.get_balance())

# Name mangling is a highly discouraged way of accessing instance
# variable outside of a class.
print("\nsavings_acc._SavingsAccount__balance:",
      savings_acc._SavingsAccount__balance)