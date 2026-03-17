import numpy

'''
Create an array containing 250 random floats
between 0 and 5:
The numpy.random module implements
pseudo-random number generators.
Samples are uniformly distributed over the half-open
interval [low, high) (includes low, but excludes high).

The word uniformly in this context tells us that
each generated random float will statisfy the
conditions set by the half-open [low, high)
interval.'''
dataset = numpy.random.uniform(0.0, 5.0, 250)

# "dataset" will consist of something like:
# 3.87388029e+00 -> 3.87388029
# 3.70518363e+00
# ...
# 4.47000569e+00
# 2.83101318e+00

print(f'Dataset: {dataset}')