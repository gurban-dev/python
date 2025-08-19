# The data type of "name" variable
# is a string.

# Indexes (always begins with zero):
#       012345678901
name = "Jack Sparrow"
#       123456789012

# Output the length of "name".
# The length is the number of characters in
# the string it was assigned.
print(f'len(name): {len(name)}')

# The program can enter only one of these blocks.
if len(name) < 3:
  print("Name must be at least 3 characters.")
elif len(name) > 50:
  print("Name can be a maximum of 50 characters.")
else:
  print("Name looks good!")