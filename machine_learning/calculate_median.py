import numpy

# Notice how the integers in this array are unsorted.
# The median() method will automatically sort them
# before finding the median or midpoint.
# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103, 111
speed1 = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

# 77, 78, 85, 86, 86, 86, 87, 87, 88, 94, 99, 103
speed2 = [99, 86, 87, 88, 86, 103, 87, 94, 78, 77, 85, 86]

median_of_speed1 = numpy.median(speed1)

# (86 + 87) / 2 = 86.5
median_of_speed2 = numpy.median(speed2)

# To remove the automatic newline at the end
# of a Python print() method, add end='' as
# the last argument.
# Adding whitespace characters affects the
# output.
print(f'median_of_speed1: {median_of_speed1}', end='')
print(f'median_of_speed2: {median_of_speed2}')