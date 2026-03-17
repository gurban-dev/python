import numpy

ages = [5, 31, 43, 48, 50, 41, 7, 11, 15, 39, 80,
        82, 32, 2, 8, 6, 25, 36, 27, 61, 31]

# Seventy-five percent of the ages are younger
# than the value of "seventy-fifth".
seventy_fifth = numpy.percentile(ages, 75)

ninetieth = numpy.percentile(ages, 90)

print(f'Seventy fifth percentile: {seventy_fifth}')

print(f'Ninetieth percentile: {ninetieth}')