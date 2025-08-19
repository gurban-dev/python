# This program demonstrates a simple for loop
# that uses a list of numbers.

# [1, 2, 3, 4, 5] is a list data structure
# in Python.

# Traverse the items/elements in the list.

print('I will display the numbers 1 through 5.')

# This for loop iterates exactly 5 times because
# there are 5 elements inside of the list that it
# iterates over. Remember that a list is an iterable.
for num in [1, 2, 3, 4, 5]:
  '''
  On each iteration, the "num" variable will be
  assigned the value of the current item/element
  in the [1, 2, 3, 4, 5] list.
  
  The print() function will output the value of
  the "num" variable.
  
  The print() function automatically appends a
  newline escape sequence at the end of the
  output.'''
  print(num)

#   print(num, end=' ')
# print('')