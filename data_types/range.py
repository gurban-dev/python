'''
range() is a built-in function that creates an iterable,
an object that holds a sequence of values you can loop over.

Syntax for the range() function:
range(start_index, stop_index (exclusive), step_value)

If you provide one argument, it becomes the stop_index.

The start_index defaults to 0.

The step_value defaults to 1.

range(5) returns:
0 1 2 3 4
'''

print('for num in range(5):')
for num in range(5):
  if num != 4:
    print(num, end=', ')
  else:
    print(num)
print('')

print('for num in range(0, 5, 1):')
for num in range(0, 5, 1):
  if num != 4:
    print(num, end=', ')
  else:
    print(num)
print('')

'''
When two arguments are passed to the range() function,
the first argument is used as the starting value of
the sequence, and the second argument is used as the
ending limit.

The for loop below begins at 1 and stops a 5 without
outputting five.
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
  print(f'num: {num}')
print('')

# The underscore (_) acts as a throwaway variable.
# It's used when a variable is required by syntax,
# but its value won't be accessed anywhere in the code.
for _ in range(5):
  print('Hello world')
print('')