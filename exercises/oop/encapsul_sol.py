# Use Decimal instead of float for money to avoid precision errors.
# Floats cannot exactly represent many decimal values (e.g., 0.1),
# which can lead to rounding issues in financial calculations.

# For instance, the subsequent expression returns True:
# 0.1 + 0.2 != 0.3
from decimal import Decimal


class BankAccount:
    def __init__(self, account_holder: str, account_number: str):

        self.account_holder = account_holder
        self.account_number = account_number

        # Initialise balance as Decimal.
        self.__balance = Decimal("0.0")

        # A list of tuples.
        self.__transactions = []

    def deposit(self, amount: float):
        # Convert to Decimal safely.
        amount = Decimal(str(amount))

        # Validate that the deposit is positive.
        if amount > 0:
            self.__balance += amount

            print(f"Successfully deposited {amount} dollars.")

            if amount > Decimal("250000"):
                print("Warning: The FDIC only insures up to 250000\n"
                      "dollars in your bank account!")

            print()

            self.add_transaction("DEPOSIT", amount)
        else:
            raise ValueError("The deposit amount must be positive.")

    def withdraw(self, amount: float):
        # Convert to Decimal safely.
        amount = Decimal(str(amount))

        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds.")

        # Update the account balance.
        self.__balance -= amount

        # Record the transaction.
        self.add_transaction("WITHDRAW", amount)

    def get_balance(self) -> Decimal:
        return self.__balance

    def get_transaction_history(self):
        # Returns a shallow copy to prevent the original from being modified.
        return self.__transactions.copy()
    
    def add_transaction(self, t_type: str, amount: Decimal):
        # Record a transaction in a controlled way.
        self.__transactions.append((t_type, amount, self.__balance))

    def transfer_to(self, other_account, amount: float):
        # Prevent invalid object type.
        if not isinstance(other_account, BankAccount):
            raise TypeError("The target must be a BankAccount.")
    
        amount = Decimal(str(amount))

        if amount <= 0:
            raise ValueError("The transfer amount must be positive.")

        if amount > self.__balance:
            raise ValueError("Insufficient funds to complete the transfer.")

        # acc1.transfer_to(acc2, 300)
        # In the context of the above line, 'self' references the same
        # object that 'acc1' references because the withdraw() method
        # is being invoked on 'acc1'.
        self.withdraw(amount)

        other_account.deposit(amount)

    def apply_interest(self, rate: float):
        # Convert to Decimal safely.
        rate = Decimal(str(rate))

        if rate <= 0:
            raise ValueError("The interest rate must be positive.")
        else:
            interest = self.__balance * rate

            self.__balance += interest

            self.add_transaction("INTEREST", interest)


if __name__ == "__main__":
    acc1 = BankAccount("Alice", "123")
    acc2 = BankAccount("Bob", "456")

    acc1.deposit(1000)
    acc1.withdraw(200)
    acc1.transfer_to(acc2, 300)

    print("Alice balance:", acc1.get_balance())
    print("Bob balance:", acc2.get_balance())

    print("\nTransaction history (Alice):")
    print(acc1.get_transaction_history())

    print("\nAttempting security breach...")
    acc1.__balance = 1_000_000
    print("Balance after hack attempt:", acc1.get_balance())

"""
REFLECTION QUESTIONS

1. Why return a copy of transaction history?
   If you return the original list, someone could do the following:
   acc1.get_transaction_history().append(("HACK", 999999, 999999))

2. How does name mangling work in Python?
   Internally, Python renames self.__balance to self._BankAccount__balance.

   This way, when someone attempts acc1.__balance = 1_000_000, the instance
   variables stays unchanged.

3. Is Python encapsulation (E.g. self.__balance) truly secure?
   No because this is convention-based protection.

   A user can still modify the instance variable by doing:
   acc1._BankAccount__balance = 1_000_000

4. How would this differ in Java/C++?
   Unlike Python, Java and C++ have strict access modifiers.

   Java and C++ use private, protected and public access modifiers.

   There is no way to directly access a private or protected
   attribute outside of a class these languages.
"""