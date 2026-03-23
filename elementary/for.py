# Repetition structure
# One or multiple lines of code in a section of
# the program will be executed one or multiple
# times.

# Python's built-in range() function accepts an
# integer (a number without quotes and without a
# decimal point), and returns an iterable or a
# collection of numbers.

# range(3) means: "Start at 0, stop at 3 (exclusive),
# and step up by 1."

# So this loop will run 3 times (from 0 to 2).
for i in range(3):
	# This will print "Ania" every time
	# the loop runs.
	print('Ania')

	# This shows which loop number we are on.
	print('i:', i, '\n')

# The subsequent line is a list data structure:
# ['Sofiia', 0, 1, 2]

# This is a list because the items are separated by commas
# and surrounded by square brackets [].

# On the 1st iteration, the variable named 'element'
# is assigned the string literal 'Sofiia'.

# On the 2nd iteration, 'element' is assigned the integer
# literal 0.
for element in ['Sofiia', 0, 1, 2, 3]:
  	print('element:', element)

print('\nPrinting for i in range(0, 3, -1):')
for i in range(0, 3, -1):
	# This loop never runs because the range is empty.

	# range(0, 3, -1) starts at 0 and moves backward by -1,
	# but the stop value (3) is greater than the start value.

	# Since the step is negative, Python expects the start
	# to be greater than the stop — which is not the case here.

	# Therefore, list(range(0, 3, -1)) returns an empty list.

	# Note that the step value cannot be 0.

	print('i:', i)

	print('Printing line 53.\n')