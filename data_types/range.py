'''
range() is a built-in function that creates an iterable,
an object that holds a sequence of values you can loop
over.

Syntax for the range() function when passing three arguments:
range(start_value, stop_value (exclusive), step_value)

The stop_value cannot be zero.


If you provide one argument, it becomes the stop_value.

The start_value defaults to 0.

The step_value defaults to 1.

The step value controls how much the number changes between
each value in the sequence. This is the increment or decrement
size.

range(5) returns:
0 1 2 3 4
'''

print('for num in range(5):')
for num in range(5):
	if num != 4:
		# 'num' is a positional argument because the name of the
		# parameter is not included.

		# end=', ' is a keyword argument because the name of the
		# parameter (end) is included.
		print(num, end=', ')
	else:
		print(num)

# A print() function without any arguments just adds
# an empty line to the output.
print()

print('for num in range(0, 5, 1):')
for num in range(0, 5, 1):
	if num != 4:
		print(num, end=', ')
	else:
		print(num)
print('')

'''
When two arguments are passed to the range() function,
the first argument is used as the start value of the
sequence, and the second argument is used as the stop
value.

The for loop below begins at 1 and stops a 5 without
including 5.
'''
print('for num in range(1, 5):')
for num in range(1, 5):
	if num != 4:
		print(num, end=', ')
	else:
		print(num)
print('')

# A list data structure is an iterable.
for num in [0, 1, 2, 3, 4]:
	# The lowercase f indicates that the following is an
	# F-string.
	print(f'num: {num}')
print('')

# The underscore (_) acts as a throwaway variable.
# It's used when a variable is required by syntax,
# but its value won't be accessed anywhere in the code.
for _ in range(5):
	print('Hello world')