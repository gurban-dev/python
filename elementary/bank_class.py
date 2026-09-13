# An object is a single unit that contains data and actions
# that can get or update that data.

# A class is a blueprint for an object.

# A class header is supposed to have two blank lines
# above it according to the PEP 8 style guide.

# A class header must begin with the class keyword followed
# by the name of the class and lastly followed by a colon:
# class <NameOfClass>:

# Notice how the name of the class is written in the PascalCase
# naming convention.

# Meaning that the first letter of each word is uppercase.


class BankAccount:
    # A class typically will have a constructor method.

    # A constructor is responsible for initialising the state
    # of an object.

    # A constructor method must have two leading and trailing
    # underscores (__).
    def __init__(self, balance_par):
        # The par (short for parameter) is to distinguish
        # balance_par from self.balance.
        print("balance_par:", balance_par)

        # self.balance belongs to the object or instance of the
        # class.

        # balance_par (without self.) is a parameter that allows this
        # constructor method to accept data from outside of the
        # class when an instance of this class is created.
        self.balance = balance_par

# Create an instance/object of the BankAccount class.
dennis_account = BankAccount(1_000)