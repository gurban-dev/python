# A tuple is an immutable data structure in Python.
# Once it is initialised, its items/elements cannot
# be mutated later on.

# Tuples have the ability to store items that are
# different data types.

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
social_security_beneficiary[0] = 112223333