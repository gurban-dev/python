# The data type of "name" variable
# is a string.

# Indexes/indices (always begins with zero):
#            012345678901
full_name = "Jack Sparrow"
#            123456789012

# Output the length of "name".
# The length is the number of characters in
# the string it was assigned.
print(f'len(full_name): {len(full_name)}')

# Access the first character or letter.
print('\nfull_name[0]:', full_name[0])

# Access the last character.
print('\nfull_name[-1]:', full_name[-1])

print('\nfull_name[len(full_name)-1]:', full_name[len(full_name)-1])

# The program can enter only one of these blocks.
if len(full_name) < 3:
	print("\nName must be at least 3 characters.")
elif len(full_name) > 50:
	print("\nName can be a maximum of 50 characters.")
else:
	print("\nName looks good!")