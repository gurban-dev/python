# Global namespace pollution...

# Import everything from math.__all__.

# -math.__all__ is a attribute that references a list that contains
# all of the function that are built into the math module.

# The asterisk (*) indicates that everything will be imported.
from math import *

'''
With from math import *, the global namespace would look roughly like:
{
    'sin': <built-in function sin>,
    'cos': <built-in function cos>,
    'sqrt': <built-in function sqrt>,
    'pi': 3.14159,
    ...
}

There are now fifty-four new names all located at the same level
as your variables.

A cleaner way to use functions defined in the math module:
import math

The namespace would roughly look like:
{
  'math': <module math>,
  ...
}

One name.
All math symbols live behind the 'math.' prefix.

'sqrt' is now the math.sqrt() function.

A namespace is a place where names exist and are associated with variables,
functions, and classes, so that they can be used.
'''
print('sqrt(16):', sqrt(16), '\n')

# Accidentally overwrite it the math.sqrt() function.
sqrt = 10

try:
    # Now 'sqrt' is an int, not a function.
    print('sqrt(16):', sqrt(16))
except TypeError as err:
    print(f'Type error: {err}')