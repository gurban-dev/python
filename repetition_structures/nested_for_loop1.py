'''
The "minutes" variable in the outer for loop
will be assigned 0 and 1 because 2 was passed
as an argument to the range() function in the
for clause.

range(2) iterate from numbers 0 to 2, but do
not include the number 2.

range(0, 2) has the same meaning.
Start: 0
Stop (without including): 2

minutes = 0
  seconds = 0
  seconds = 1
minutes = 1
  seconds = 0
  seconds = 1
'''

no_of_iterations = 0

# range(2) will generate
# the following iterable:
# [0, 1]
print('range(2):', range(2))

'''
This nested for loop will iterate twice two
times.

The inner loop will iterate twice and
the outer loop tells us to iterate
twice for a total of two times.

The value of "minutes" increasing indicates
that the program is currently executing the
outer for loop.'''
for minutes in range(2):
  '''
  The program will not move on to the next
  iteration of the outer for loop until the
  program has finished executing all of the
  iterations in the inner for loop.

  The incrementation of the "minutes" variable
  only occurs after the completion of the inner
  for loop.
  
  After the inner for loop competes its two
  iterations, the "seconds" variable will be
  assigned values starting from the beginning
  of range(2) again.'''

  for seconds in range(2):
    '''
    When the value of "seconds" increases,
    yet the value of "minutes" stays the same,
    that tells us that the program is currently
    inside of the inner for loop.'''
    print('\nminutes:', minutes,
          '\nseconds:', seconds)

    no_of_iterations += 1

print(f'\nno_of_iterations: {no_of_iterations}')

'''
The total number of iterations is equal to the
number of iterations in the outer for loop
multiplied by the number of iterations in the
inner for loop.

Time complexity: O(n^2)
'''