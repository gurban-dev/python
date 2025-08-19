"""
There are two variables in this program:
x and y

The data type of variable "x" is an integer
because an integer value, namely 10 was
assigned to it.

The same can be said of variable "y".
"""
x = 10

'''
A variable can be thought of as a box capable
of storing a single value in memory.
x = x + 3 -> x = 10 + 3 -> x = 13

+= is called an augmented assignment operator.
'''
x += 3
print("x:", x)

# To demonstrate the format:
# print('variable_name:', variable_name)

y = 10

"""
Assign the current value of variable
"y" minus 3 to variable "y".

y = y - 3 -> y = 10 - 3 -> y = 7
"""
y -= 3
print("y:", y)

"""
Float division will give you the
exact amount of times a number can
fit into a larger number.

This means that you may see the remainder
included in the calculation which makes it
more precise that integer division.

In programming, a decimal number is referred
as a floating point number.

E.g. 3.3333333333333335
"""

# Float division
# Output:
# 10 / 3: 3.3333333333333335
print("10 / 3:", 10 / 3)

"""
Integer/floor division is going to give
you the amount of times a number can
fully go into a larger number."""

# Integer/floor division
print("10 // 3:", 10 // 3)

# Multiplication
print("10 * 3:", 10 * 3)

# Exponentation
# Equivalent of 10^3.
print("10 ** 3:", 10 ** 3)

"""
Used to get the remainder of a division.
Always returns a whole number or an integer.

Returns the remainder of 10 divided
by 3 if there is any.

3 goes into 10 three times.

3 x 3 = 9

10 - 9 = 1

10 is congruent to 1 mod 3.

10 - 1 = 9 and 9 is a multiple of 3
which makes it fully divisble by 3.
"""
# 10 modulo 3
print('10 % 3:', 10 % 3)