# Import the module named "numpy".
import numpy

# An array/Python list.
speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# The mean is also referred to as the "average".
mean_of_speed = numpy.mean(speed)

# Insert the variable "mean_of_speed"
# in between the curly braces within
# the F-string (formatted string literal).
print(f'mean_of_speed: {mean_of_speed}')