'''
Boolean values

In Python, the two explicit boolean values are True and False.

Assigning True or False to a variable makes that variable reference
to a boolean value:
is_logged_in = True
is_admin = False

Python can also interpret other values as either True or False.

This is called truthiness.

Every Python value can be evaluated in a boolean context.

Truthy values evaluate to True.
Falsy values evaluate to False.

The bool() function lets us see the boolean interpretation of a value:
bool(1)       # True
bool(0)       # False
bool("hello") # True
bool("")      # False

Python has a particularly close relationship between integers and
booleans because bool is a subclass of int:
isinstance(True, int)   # True
isinstance(False, int)  # True

Assigning any of the following falsy values will make a variable
be interpreted as False.

Examples of falsy values:
Empty strings: '', ""

Integer zero: 0

Floating-point zero: 0.0

Constants: None

Empty lists: []

Empty tuples: ()

Empty dictionaries: {}

Empty sets: set()

Empty ranges: range(0)


Examples of truthy values:
Non-empty strings: "False", " ", ' '

Non-zero integers: -1

Non-zero floats: -1.5

Non-empty lists: [1, 2, 3]

Non-empty tuples: (1, 2, 3)

Non-empty dictionaries: {"a": 1, "b": 2}

Non-empty sets: {1, 2, 3}

Non-empty ranges: range(1, 10)
'''

'''
An empty string evaluates to False.
\' is one of the escape sequences in Python.

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

# The "None" keyword represents the absence of
# a value. It has the same meaning as null.
# This evaluates to False.
refresh_token = None

# What needs to be changed for refresh_token to be
# interpreted as False?
refresh_token = 'random content'

'''
The program enters the indented block directly under
the "if" keyword if "refresh_token" evaluates to True.

The program will enter the else block if "refresh_token"
evaluates to False.'''
if refresh_token:
  print('refresh_token evaluated to True.')
else:
  print('refresh_token evaluated to False.')