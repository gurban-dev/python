'''
A library is a collection of Python files that contain
functions that can be used in Python programs.

These Python files are also called modules.
'''

# numpy is the library being used in this case.
# np is an alias for the numpy library.

# numpy can be installed with the subsequent command:
# pip install numpy
import numpy as np

# To invoke a function from a library, the name of the function
# must be preceded with the alias of the library.
floor_of_one_point_five = np.floor(1.5)

print('floor_of_one_point_five:', floor_of_one_point_five)