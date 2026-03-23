class BankAccount:
	# The two underscores that precede the class and instance
	# varibles indicate that they should be treated as private.

	# Class variable/attribute.
	__bank_name: str = "JP Morgan Chase"

	def __init__(self):
		# Instance variable/attribute.
		self.__balance: float = 1.0
	
	# Selector/getter
	def get_account_balance(self) -> float:
		return self.__balance

	# Mutator/setter
	def set_account_balance(self, amount: float) -> None:
		self.__balance: float = amount

	@classmethod
	def get_bank_name(cls) -> str:
		return cls.__bank_name

	@classmethod
	def set_bank_name(cls, new_bank_name) -> None:
		cls.__bank_name: str = new_bank_name

bankAccountObj = BankAccount()

# Both of the commented out instructions fail due to the attributes
# being name mangled.
# bankAccountObj.__bank_name = "Union Bank of Switzerland"

# print(bankAccountObj.__bank_name)

# bankAccountObj.__account_balance = 2.0

# print(bankAccountObj.__account_balance)

# Legal, but the improper way to access and mutate an object's state/data.
bankAccountObj._BankAccount__bank_name = "Union Bank of Switzerland"

bankAccountObj._BankAccount__balance = 2.0

print('bankAccountObj._BankAccount__bank_name:', bankAccountObj._BankAccount__bank_name)

print('\nbankAccountObj._BankAccount__balance:', bankAccountObj._BankAccount__balance)

# The proper way involves invoking the class and instance methods:
print('\nbankAccountObj.set_account_balance(2.0):', bankAccountObj.set_account_balance(2.0))

print('\nbankAccountObj.get_account_balance():', bankAccountObj.get_account_balance())

print('\nbankAccountObj.set_bank_name(\"Union Bank of Switzerland\"):',
      bankAccountObj.set_bank_name("Union Bank of Switzerland"))

print('\nbankAccountObj.get_bank_name():', bankAccountObj.get_bank_name())