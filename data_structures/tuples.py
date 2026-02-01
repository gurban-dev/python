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

# Question:
# If I am assigning the same exact integer, why
# is this illegal?

# Answer:
# Python doesn't care about the value of what you're
# assigning, it simply forbids assignment to an index
# inside of a tuple.

# Similar to tuples, strings, integers and floats are also
# immutable in Python.

str1: str = "a"
str2: str = "a"
str3: str = "A"

print('\nhex(id(str1)):', hex(id(str1)))
print('hex(id(str2)):', hex(id(str2)))
print('hex(id(str3)):', hex(id(str3)))

int1: int = 10
int2: int = 10
float1: float = 10.0
float2: float = 10.0

# Print the identity of these three variables.
print('hex(id(int1)):', hex(id(int1)))
print('hex(id(int2)):', hex(id(int2)))

print('\nhex(id(float1)):', hex(id(float1)))
print('hex(id(float2)):', hex(id(float2)))