# "m" is the alias for the math module.
# Keep in mind that an alias is not mandatory.
# Meaning that it is optional.
import math as m

'''
Syntax: round(number, number_of_digits)

number: number to be rounded
number_of_digits (Optional): number of digits
up to which the given number is to be rounded.

Returns either a float or an integer.

If a value for the second argument is not
provided, the number is automatically rounded
to an integer.'''

x = 2.85
print("round(x):", round(x))

'''
Syntax: abs(number)

number: Integer, floating-point number, complex number.

Return the absolute value which could be either an
integer or float.'''

y = -2.9
print("abs(y):", abs(-2.9))

'''
Syntax:
import math
math.ceil(number)

Returns the smallest integer greater than or equal
to "number".'''

z = 1.9
print("math.ceil(z):", m.ceil(z))

'''
Syntax:
import math
math.floor(number)

Returns the largest integer not greater than "number".
'''

q = 1.9
print("math.floor(q):", m.floor(q))