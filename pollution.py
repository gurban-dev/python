# Global namespace pollution happens when too many names (variables,
# functions, classes, etc.) are placed into the program’s global
# scope, increasing the chance that names will conflict, overwrite
# each other, or make the code harder to understand.

# Import all names listed in math.__all__ into the current namespace.

# __all__ defines which names are imported when from module import
# * is used.

# The asterisk (*) indicates that everything will be imported.
from math import *

'''
With from math import *, the global namespace would look roughly like:

{
    'sin': <function math.sin>,
    'cos': <function math.cos>,
    'sqrt': <function math.sqrt>,
    'pi': 3.141592653589793,
    ...
}

There are now dozens of new names at the same level as your variables.

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

# Accidentally overwrite the math.sqrt() function.
sqrt = 10

try:
    # Now 'sqrt' is an int, not a function.
    print('sqrt(16):', sqrt(16))
except TypeError as err:
    print(f'Type error: {err}')