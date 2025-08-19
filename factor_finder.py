'''
This program finds all the factors of a number.
This code is available at the succeeding link:
https://inventwithpython.com/bigbookpython/project24.html
'''

'''
math is a Python module that comes with functions
that execute mathematical operations like calculating
square root of a number for example.

sys is a module that provides access to some variables
used or maintained by the interpreter.
'''
import math, sys

print('''
A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.

Can you discover some prime numbers?''')

# while True and while 1 are both infinite loops.
while 1:
  print('\nEnter a positive whole number to factor (or QUIT):')

  # Get input from the end user.
  response = input('> ')

  '''
  Verify whether the end user chose to quit the program.
  Even if the user inputs "quit", the program will
  terminate because the upper() is invoked to capitalise
  the "response" string variable.'''
  if response.upper() == 'QUIT':
    sys.exit()

  '''
  Since the "not" keyword precedes the if statement,
  response.isdecimal() evaluating to true will short
  circuit the if statement because the latter condition
  doesn't need to be evaluated due to the program already
  knowing what the entire condition will evaluate to.

  short circuit can be interpreted as once the program
  knows what the entire if statement will evaluate to,
  the evaluation ceases to persist.

  In both if statements with the "and" and "or" keyword,
  conditions are evaluated from left to right. Meaning
  that the condition on the left side of the "and" or
  "or" is evaluated first and then the one on the right
  side is evaluated.

  The isdecimal() method returns True if all the
  characters are decimals (0-9). This means that
  if there is a decimal point character or any
  character, false will be returned.

  E.g.
  response = '10'
  print(response.isdecimal()) -> True

  response = '1.0'
  print(response.isdecimal()) -> False

  response = '-1'
  print(response.isdecimal()) -> False
  '''

  try:
    print(f'\nresponse.isdecimal(): {response.isdecimal()}')
    print(f'int({response}) > 0: {int(response) > 0}\n')

    '''
    if not is the same as saying if the condition
    is false.

    If the response.isdecimal() and int(response) > 0
    conditions are both false, the program will enter
    the body of the if statement.

    int('1.0') > 0 was generating an exception.
    '''
    if not (response.isdecimal() and int(response) > 0):
      # Try inputting -1.
      print(f'response.isdecimal() and int({response}) > 0 are both false.')

      '''
      The continue keyword is used to end the current
      iteration in a for loop or a while loop, and
      continue to the next iteration.
      '''
      continue
  except ValueError:
    print('\nYou cannot input a number with a decimal point.')

    continue

  '''
  Cast the "response" string variable as an integer.
  This variable was a string because the input()
  returns a string by default.
  '''
  number = int(response)

  # "factors" declared on the subsequent or next
  # line is a Python list data structure.
  factors = []

  # Find the factors of the inputted number.
  # start: 1, stop_and_exclude: int(math.sqrt(number)) + 1
  for i in range(1, int(math.sqrt(number)) + 1):
    # If there's no remainder, then
    # "i" is a factor of "number".

    # First iteration:
    # 9 % 1 == 0
    if number % i == 0:
      # factors.append(1)
      factors.append(i)

      # factors.append(9 // 1)
      # // is integer division.
      # factors.append(9)
      factors.append(number // i)

  # Convert to a set to get rid of duplicate factors.
  factors = list(set(factors))

  # Sort the "factors" list in ascending order.
  factors.sort()

  # enumerate() will return both the index and
  # value of the item/element on each iteration.
  for index, factor in enumerate(factors):
    print(f'index: {index}, factor: {factor}\n')

    # Cast the integer values inside the "factors"
    # list as strings, so that the "factors" list
    # is now composed of strings rather than integers.
    factors[index] = str(factor)
  print(', '.join(factors))