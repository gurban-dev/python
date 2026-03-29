"""
Concepts:
Encapsulation
Name mangling

Secure Banking System

Objective:
Design a secure banking system that demonstrates strong use
of encapsulation in Python.

Instructions:
- Read all requirements carefully.
- Implement the BankAccount class below.
- DO NOT modify method names or signatures.
- Follow all encapsulation rules strictly.


REQUIREMENTS

1. Core Class: BankAccount

Each account must store:
- account holder name
- account number
- balance (PRIVATE)
- transaction history (PRIVATE)

Encapsulation rules:
- No direct access to balance or transactions
- Use name mangling (e.g., __balance)

-----------------------------------------------------------

2. Public Methods to Implement

deposit(amount)
- Add money
- Reject zero or negative values

withdraw(amount)
- Deduct money if sufficient funds
- Prevent overdrawing

get_balance()
- Return current balance (read-only)

get_transaction_history()
- Return a COPY of the transaction history

-----------------------------------------------------------

3. Advanced Requirements

A. transfer_to(other_account, amount)
- Transfer money safely
- Must use public methods only
- Must be atomic (no partial updates)

B. Immutable Transactions
Each transaction should be stored as:
(type, amount, resulting_balance)

- Must NOT be modifiable after creation

'type' represents the kind of transaction.

E.g.
("WITHDRAW", 200, 800)

C. apply_interest(rate)
- Apply interest to balance
- Only if rate > 0

D. Security Test
Try:
    account.__balance = 1000000

Explain why this does NOT actually modify the real balance.

-----------------------------------------------------------

4. Expected Example Usage

acc1 = BankAccount("Alice", "123")
acc2 = BankAccount("Bob", "456")

acc1.deposit(1000)
acc1.withdraw(200)
acc1.transfer_to(acc2, 300)

print(acc1.get_balance())  # Expected: 500
print(acc2.get_balance())  # Expected: 300


Complete the class below.
"""

class BankAccount:
    def __init__(self, account_holder: str, account_number: str):
        # TODO: Initialize attributes
        # - public: account_holder, account_number
        # - private: __balance, __transactions
        pass

    def deposit(self, amount: float):
        # TODO:
        # - Validate amount > 0
        # - Update balance
        # - Record transaction
        pass

    def withdraw(self, amount: float):
        # TODO:
        # - Validate amount > 0
        # - Check sufficient balance
        # - Update balance
        # - Record transaction
        pass

    def get_balance(self) -> float:
        # TODO:
        # - Return balance (read-only)
        pass

    def get_transaction_history(self):
        # TODO:
        # - Return a COPY of transaction list
        pass

    def transfer_to(self, other_account, amount: float):
        # TODO:
        # - Use withdraw and deposit methods
        # - Ensure atomic behavior
        pass

    def apply_interest(self, rate: float):
        # TODO:
        # - Apply interest if rate > 0
        pass


if __name__ == "__main__":
    acc1 = BankAccount("Alice", "123")
    acc2 = BankAccount("Bob", "456")

    # Basic tests (should work after implementation)
    acc1.deposit(1000)
    acc1.withdraw(200)
    acc1.transfer_to(acc2, 300)

    # Expected: 500
    print("Alice balance:", acc1.get_balance())

    # Expected: 300
    print("Bob balance:", acc2.get_balance())

    # Security test
    print("\nAttempting security breach...")
    acc1.__balance = 1000000
    print("Balance after hack attempt:", acc1.get_balance())

"""
REFLECTION QUESTIONS

1. Why return a copy of transaction history?
2. How does name mangling work in Python?
3. Is Python encapsulation truly secure?
4. How would this differ in Java/C++?
"""