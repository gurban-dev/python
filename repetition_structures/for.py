# This program demonstrates a simple for loop
# that iterates through a list of numbers.

# [1, 2, 3, 4, 5] is a list data structure in
# Python.

# Traverse the items/elements in the list.

print('The numbers 1 through 5:')

# This for loop iterates exactly 5 times because
# there are 5 elements inside of the list that it
# iterates over. Remember that a list is an iterable
# also known as a sequence of values.
for num in [1, 2, 3, 4, 5]:
  '''
  On each iteration, the "num" variable will be
  assigned the value of the current item/element
  in the [1, 2, 3, 4, 5] list.
  
  The print() function will output the value of
  the "num" variable.
  
  The print() function automatically appends a
  newline escape sequence at the end of its
  output.'''
  # print(num, end='\n')

  if num == 5:
    print(num, end='')
  else:
    print(num, end=', ')
print('\n')

# Python lists can store elements that have different
# data types.
for item in ['Alexander', 30, 20.0, True, [], range(2)]:
  print('item:', item)
print('')

# range(start (inclusive), stop (exclusive), step)

# Arguments to the range() function must be integers.
# Only the argument for the step parameter must be
# non-zero.

# The variable "i" is assigned the element from
# the current iteration.
for i in range(-1, 6, 1):
  print('i:', i)
print()

# The default step is set to 1. This means that if this
# is the behaviour your program needs to have, it is not
# necessary to explicitly write out 1 for the step parameter.
# It happens implicitly or internally.
for i in range(-1, 6):
  print('i:', i)