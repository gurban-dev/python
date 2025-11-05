# A tuple is an immutable data structure in Python.
# Once it is initialised, its items/elements cannot
# be mutated later on.

# Tuples have the ability to store items that are
# of different data types.

# Tuple data structure.
social_security_beneficiary = (
  111223333,
  '111-22-3333',
  False
)

# social_security_beneficiary is a variable that
# references the tuple that exists in memory.

print('type(social_security_beneficiary):',
  type(social_security_beneficiary))

print('\nsocial_security_beneficiary:',
  social_security_beneficiary)

# Make an attempt to mutate the first
# element of the tuple.
# social_security_beneficiary[0] = 111223333

# If I am assigning the same exact integer, why
# is this illegal?

num1: int = 10
num2: int = 10
num3: int = 11

print('\nhex(id(num1)):', hex(id(num1)))
print('hex(id(num2)):', hex(id(num2)))
print('hex(id(num3)):', hex(id(num3)))

num1: int = 10
num2: int = 10
num3: int = 11

str1: str = "a"
str2: str = "a"
str3: str = "b"

print('\nhex(id(str1)):', hex(id(str1)))
print('hex(id(str3)):', hex(id(str2)))
print('hex(id(str3)):', hex(id(str3)))