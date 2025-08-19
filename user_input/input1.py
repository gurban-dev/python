'''
The built-in input() function accepts input from
the user's keyboard and then returns that input
as a string.

Include a whitespace character after the prompt
statement because the input() function does not
automatically include one.'''
name = input('What is your name? ')

# F-string
# print('name:', name, end='')
print(f'name: {name}')

"""
Since the input() function returns a string,
adding two inputted numbers as strings will
simply concatenate them.
"1" + "2" = "12"
"""

# Input 2.
num1_str = input('\nInput a number: ')

# Input 2 again.
num2_str = input('Input a second number: ')

# The output is 22 because variables
# "num1_str" and "num2_str" are strings
# rather than integers.
# The following is known as string concatenation.
print(f'num1_str + num2_str: {num1_str + num2_str}')

"""
Invoke the int() function for the sake of
converting the string returned by the
input() function to an integer.

In this context, doing this is necessary
because addition must be performed with
numbers rather than strings.

Numeric literal: '1'

Remember that inputting a non-numerical value like
"fish" and then trying to cast it as an integer
generates a ValueError because "fish" converted to
an integer."""

# Input 2.
num1_int = int(input('\nInput a number: '))

# Input 2 again.
num2_int = int(input('Input a second number: '))

print(f'num1_int + num2_int: {num1_int + num2_int}')