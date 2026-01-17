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

# 'social_security_beneficiary' is a variable that
# references the tuple object that exists in memory.

print('type(social_security_beneficiary):',
      type(social_security_beneficiary))

# Demonstrates how the items in a tuple can be outputted.
# Like lists, tuples are ordered. Meaning that each element
# has a fixed position.
print('\nsocial_security_beneficiary:',
      social_security_beneficiary)

# Make an attempt to mutate the first element of
# the tuple. Notice how the same integer value
# is being assigned.
# social_security_beneficiary[0] = 111223333

# Tuples support indexing. They are indexable.
print("social_security_beneficiary[0]:", social_security_beneficiary[0])

# If I am assigning the same exact integer, why
# is this illegal?

# Answer:
# Python doesn't care about the value of what you're
# assigning, it simply forbids assignment to an index
# inside of a tuple.

# Similar to tuples, integers and strings are also
# immutable in Python.

num1: int = 10
num2: int = 10
num3: int = 10.0

# Print the memory addresses that these three variables
# reference.
print('\nhex(id(num1)):', hex(id(num1)))
print('hex(id(num2)):', hex(id(num2)))
print('hex(id(num3)):', hex(id(num3)))

str1: str = "a"
str2: str = "a"
str3: str = "A"

print('\nhex(id(str1)):', hex(id(str1)))
print('hex(id(str2)):', hex(id(str2)))
print('hex(id(str3)):', hex(id(str3)))