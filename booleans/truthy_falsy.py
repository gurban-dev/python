'''
Boolean values are True or False.

In Python, they are written as "True" and "False"
(without the quotes).

Assigning True or False to a variable will make
that variable a boolean variable.

In Python there are truthy and falsy values which
are not explicitly a boolean True or False, but
can be interpreted as such.

Assigning any of the following falsy values will
make a variable be interpreted as False.

Examples of falsy values:
Empty strings: '', ""

Integer zero: 0

Floating-point zero: 0.0

Constants: None

Empty lists: []

Empty tuples: ()

Empty dictionaries: {}

Empty sets: set()

Empty strings: ""

Empty ranges: range(0)


Examples of truthy values:
Non-zero numbers: -1.5

Non-empty lists: [1, 2, 3]

Non-empty tuples: (1, 2, 3)

Non-empty dictionaries: {"a": 1, "b": 2}

Non-empty sets: {1, 2, 3}

Non-empty strings: "False"

Non-empty ranges: range(1, 10)
'''

# The "None" keyword represents the absence of
# a value. It has the same meaning as null.
# This evaluates as False.
refresh_token = None

refresh_token = 'random content'

'''
An empty string evaluates as False.
\' is one of the escape sequence in Python.

Output:
bool(''): False
'''
print(f'bool(\'\'): {bool('')}')

# Another way of writing the above line.
# print(f"\nbool(''): {bool('')}")

print('\nbool(\'False\'):', bool('False'))

# -1.5 is truthy because it is not equal to zero.
# Any numeric non-zero value is truthy regardless
# of whether it is positive or negative.
print('\nbool(-1.5):', bool(-1.5), end='\n\n')

'''
The program enters the indented block directly under
the "if" keyword if "refresh_token" evaluates as True.
The program will enter the else block is "refresh_token"
evaluates as False.'''
if refresh_token:
  print('refresh_token evaluated as True.')
else:
  print('refresh_token evaluated as False.')