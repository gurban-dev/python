# Repetition structure
# One or multiple lines of code in a section of
# the program will be executed one or mutliple
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

print('')

# The subsequent line is a list data structure:
# ['Sofiia', 0, 1, 2]

# This is a list because the items are separated by commas
# and surrounded by square brackets [].

# For-loop
for element in ['Sofiia', 0, 1, 2]:
  print('element:', element)

print('')
for i in range(0, 3, -1):
  print('i:', i)

  print('Oh yeah!\n')

for expression in ['Oh', 'yeah!']:
  print(expression)