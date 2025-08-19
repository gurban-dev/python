'''
Import the math module to perform complex
mathematical calculations on numbers.

A module is a file containing Python source code.
'''
import math

'''
round() returns a number rounded to ndigits precision
after the decimal point. If ndigits is omitted or is
None, it returns the nearest integer.

Syntax: round(number, ndigits=None)
'''

# Rounded to the nearest integer.
print(f'round(2.95): {round(2.95)}')

# Rounded to two digits after the decimal point.
# ndigits is 2 in this instance.
print(f'\nround(2.95, 2): {round(2.95, 2)}')

# The built-in abs() function returns the absolute value
# of a number, meaning its non-negative value.
print(f'\nabs(-2.9): {abs(-2.9)}')

# Type "math." (without the quotes) to see all of
# the methods associated with the math object.

# The ceil() method returns the ceiling of the numeric value
# passed to it. Or, the smallest integer greater than or equal
# to it. In this context, the ceiling of 2.2 is 3.
print('\nmath.ceil(2.2):', math.ceil(2.2))

# The floor() method returns the floor of the passed numeric
# value. In other words, the largest integer less than or
# equal to the number passed as an argument.
print('\nmath.floor(2.2):', math.floor(2.2))

'''
Python documentation where a complete list of methods
associated with the math module can be found:
https://docs.python.org/3/library/math.html

The round() and abs() functions in Python are built-in
functions, meaning they are part of Python's core
functionality and do not belong to the math module.

This is why their documentation is separate from the
math module:
https://docs.python.org/3/library/functions.html
'''