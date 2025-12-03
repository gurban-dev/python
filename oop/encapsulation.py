# Encapsulation is the principle of restricting direct access
# to an object's internal state (attributes) and internal methods,
# typically using private or protected naming conventions.

# Controlled access is provided through public methods, which allow
# getting or setting the object's internal state in a safe and
# controlled way.

class BankAccount():
  def __init__(self, balance):
    # Python does not have strict access modifiers like
    # TypeScript.

    # Prefixing an attribute with __ triggers name mangling,
    # making it less accessible from outside of the class.

    # self.__balance becomes _BankAccount__balance internally.

    # Conventionally, or by standard procedure, variables that
    # that have two underscores preceding their names are treated
    # as private attributes.
    self.__balance = balance
  
  # Selector/getter method.
  def get_balance(self):
    return self.__balance
  
  # Mutator/setter method.
  def deposit(self, amount):
    # += is called the augmented assignment operator.

    # self.__balance += amount is equivalent to:
    # self.__balance = self.__balance + amount
    self.__balance += amount

bankAccount = BankAccount(5_000)

# Direct access like bankAccount.__balance fails
# because of name mangling:
# bankAccount.__balance += 500

# Preceding "balance" with two underscores in the
# constructor method makes the instance variables
# only accessible outside of the class if its name
# is preceded with _<class_name>__<instance_variable_name>

# Accessing bankAccount._BankAccount__balance directly works,
# but it's discouraged in practice.

# E.g. _BankAccount_balance
# bankAccount._BankAccount__balance += 500

bankAccount.deposit(500)

print('bankAccount.get_balance():', bankAccount.get_balance())