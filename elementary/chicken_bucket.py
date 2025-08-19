# Our first variable.
# We know that "bucket_capacity" is a variable because
# the assignment operator is to the right of it (=).

# Total pieces of chicken the bucket can hold
bucket_capacity = 4

# Since 4 is an integer literal, assigning it to
# the variable "bucket_capacity" will mean that the
# data type of this variable will be an integer.
print('type(4):', type(4))

# Current pieces of chicken
pieces_in_bucket = 4

# Scale from 1 (full) to 10 (starving)
hunger_level = 4

print("\n🍗 Welcome to Ania and Sofiia's Chicken Bucket! 🍗")

# F-string
print(f"Your bucket currently has {pieces_in_bucket} pieces out of {bucket_capacity}.")

'''
How do we know that range() is a function?

Anytime you see a name followed by parentheses,
you can conclude that it is a function.

print()
input()
range()
'''

# Remember that the "bucket_capacity" variable it
# stores the value 4, which is an integer literal.
# This is appropriate because as stated earlier, the
# range() function accepts an integer as an argument.
# range(4)

# The range() function returns an iterable.
# An iterable is a collection of numbers.
print('\nrange(4):', range(4), '\n')

# For-loop
# "i" is a variable.
# The range() function accepts an integer as an argument.

# range(bucket_capacity) becomes range(4) in this case
# because "bucket_capacity" was assigned .
for i in range(bucket_capacity):
  print('i:', i)