# Global namespace pollution...

# Import every public name listed in math.__all__.

# math.__all__ is an attribute that contains the public functions
# and constants imported by 'from math import *'.

# The asterisk (*) imports every public name listed in math.__all__.
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

There are now many new names in the global namespace alongside
the variables defined in this program.

A cleaner way to use functions defined in the math module:
import math

The namespace would roughly look like:
{
  'math': <module math>,
  ...
}

One new name.
All math symbols live behind the 'math.' prefix.

The square root function is now accessed as math.sqrt().

A namespace is a mapping between names and the objects they refer to,
such as variables, functions, classes, and modules.
'''
print('sqrt(16):', sqrt(16), '\n')

# The original function still exists inside the math module.
# Only the imported name will be replaced.

# Accidentally overwrite the imported sqrt function.
sqrt = 10

try:
    # Now 'sqrt' is an int, not a function.
    print('sqrt(16):', sqrt(16))
except TypeError as err:
    print(f'Type error: {err}')