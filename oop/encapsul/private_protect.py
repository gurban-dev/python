

class BankAccount:
    def __init__(self):
        self._balance = 1_000
    
    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    def __init__(self):
        # Call the parent class' constructor method.
        super().__init__()

        # BankAccount.__init__()

        # Unintentionally overwriting the parent's instance variable.
        # self._balance = 0

        # Create a new variable instead of overwriting the parent's.
        self.__balance = 0

acc = SavingsAccount()

# Output is 1000 because __balance in the child class does not
# overwrite _balance in the parent class. They are different
# variables.
print(acc.get_balance())