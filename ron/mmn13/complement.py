def complement(lst):
	"""
	Returns the complement of a list of natural
	numbers.

	The complement list includes all natural
	numbers from 1 to the maximum number in
	"lst" that do not appear in "lst".

	If "lst" is empty, the function returns an
	empty list.

	Constraints:
	- The function avoids use of the 'in' operator
	  for membership checks.
	- It uses basic Python constructs only (no
	  dictionaries, no sorting).
	- Assumes all elements in lst are distinct
	  natural numbers.

	Parameters
	----------
	lst : list of int
		A list of distinct natural numbers.

	Returns
	-------
	list of int
		The complement of lst from 1 to max(lst),
		inclusive.
	"""
	# Return an empty list if the input is an
	# empty string.
	if not lst:
		return []

	# Find the maximum value in "lst".
	max_value = max(lst)

	# Initialize an empty list to hold the complement.
	result = []

	# Loop through the range from 1 to max_value
	# (inclusive).
	for num in range(1, max_value + 1):
		# Flag to check if num is in "lst".
		found = False

		# Loop through "lst" to check if "num" is present.
		for value in lst:
			if value == num:
				found = True

				# No need to continue once found.
				break

		# If "num" was not found in "lst", add it to
		# the result.
		if not found:
			result.append(num)

	return result

lst1 = [1, 4, 5, 7, 8, 9]

lst2 = [1, 2, 3, 4]

lst3 = []

print('complement(lst1):', complement(lst1))

print('\ncomplement(lst2):', complement(lst2))

print('\ncomplement(lst3):', complement(lst3))