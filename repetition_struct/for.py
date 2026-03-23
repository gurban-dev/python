# One of the repetition structures in Python is called a for loop.

# A for loop executes a block of source code zero or more times.
# A for loop in Python iterates over an iterable (an object that
# can return values one at a time).

# [1, 2, 3, 4, 5] is a list data structure in Python.

# Traverse the items/elements in the list.

print('for num in [1, 2, 3, 4, 5]:')

# This for loop iterates exactly 5 times because there are 5
# elements inside of the list that it iterates over. Remember
# that a list is an iterable also known as a sequence of values.
for num in [1, 2, 3, 4, 5]:
	'''
	On each iteration, the 'num' variable will be assigned the
	value of the current item/element in the [1, 2, 3, 4, 5] list.
	
	The print() function will output the value of the 'num' variable.
	
	The print() function automatically appends a newline escape
	sequence at the end of its output.'''
	# print(num, end='\n')
	# print(num)

	# The following is the equality operator: ==

	# It returns True if the operands it compares are seen as equal
	# by Python. Otherwise, it returns False.
	if num == 5:
		print(num, end='')
	else:
		print(num, end=', ')
print('\n')

# Python lists can store elements that have different data types.
for item in ['Alexander', 30, 20.0, True, [], range(2)]:
	print('item:', item)
print('')

# range(start (inclusive), stop (exclusive), step)

# Arguments to the range() function must be integers.
# Only the argument for the step parameter must be
# non-zero.

# The start value defaults to 0 (zero) when only one argument
# is passed to the range() function. The step value default to
# 1 in this case.

# The stop value is simply the one argument that was passed to
# the range() function.

print('Printing for i in range(6):')
for i in range(6):
	if i != 5:
		print(i, end=", ")
	else:
		print(i, end="")
print()

# In the case that the range() function is given three arguments:
# The start value is the first argument.
# The stop value (exclusive) is the second argument.
# The step value is the third argument.

print('\nPrinting for i in range(-1, 6, 1):')

# Start value: -1
# Stop value (exclusive): 6 (5 is the last integer in the range)
# Step value: 1

# The variable "i" is assigned the element from the current iteration.
for i in range(-1, 6, 1):
  print('i:', i)

# In the case that the range() function is given two
# arguments:
# The start value is the first argument.
# The stop value (exclusive) is the second argument.
# The step value is implicitly 1 by default.

print('\nPrinting for i in range(-1, 6):')

# The default step value is set to 1. This means that if this is
# the behaviour your program needs to have, it is not necessary
# to explicitly write out 1 for the step parameter. It happens
# implicitly or internally.
for i in range(-1, 6):
	print('i:', i)