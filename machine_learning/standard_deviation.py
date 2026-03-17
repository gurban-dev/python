# Import "numpy" module.
import numpy as np

speed1 = [86, 87, 88, 86, 87, 85, 86]
speed2 = [32, 111, 138, 28, 59, 77, 97]

std_deviation1 = np.std(speed1)

# The standard deviation for speed2 is 37.85, indicating
# that most of the values are within the range of 37.85
# from the mean value, which is 77.4.
std_deviation2 = numpy.std(speed2)

print(f'std_deviation1: {std_deviation1}')

# The round() method is used to handle the
# precision of floating point numbers.
print(f'std_deviation2: {round(std_deviation2, 2)}')