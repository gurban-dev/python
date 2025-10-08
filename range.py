'''
Python provides a built-in function named range() that
simplifies the process of writing a count-controlled
for loop. The range() function creates a type of object
known as an iterable.

An iterable is an object that is similar to a list.
It contains a sequence of values that can be iterated
over with something like a loop.

If you pass one argument to the range() function, that
argument is used as the ending limit of the sequence
of numbers.
'''
print('for num in range(5):')
for num in range(5):
  if num != 4:
    print(num, end=', ')
  else:
    print(num)
print('')

# range(start, stop (exclusive), step)
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