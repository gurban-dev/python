while True:
	# The .strip() method will remove the leading and trailing
	# whitespace characters from a string:
	# "   Alexander  ".strip() returns "Alexander"
	given_name = input('Enter your given name: ').strip()

	# In Python, there are truthy and falsy values.
	# Or, values that are not explicitly True or False, but
	# that can be interpreted that way.

	# If given_name is an empty string, it is interpreted as False.
	# If given_name is assigned a string that has a length that
	# is greater than zero, it is interpreted as True.

	print(f'bool(given_name): {bool(given_name)}')

	if given_name:
		break
	else:
		print('\nError! You must input a given name. Try again.')