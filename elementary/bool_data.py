# Assigning "False" or "True" (without the quotation
# marks), to a variable, makes the data type of the
# variable a boolean.
lives_in_france = False

has_been_to_france = True

# The type() function can be used to determine the data
# type of a variable.

# To see the data type of the variable "lives_in_france",
# pass it as an argument to the type() function.
print('type(lives_in_france):', type(lives_in_france))

# The newline escape sequence ('\n') adds a newline
# to the output of a Python program.
print('\ntype(has_been_to_france):', type(has_been_to_france))

print('\ntype(True):', type(True))

print('\ntype(False):', type(False))