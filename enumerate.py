# Indices:  0  1  2
lst: int = [1, 2, 3]

# The largest index, also the last index, in an iterable
# (sequence of values), is always one less than size of
# the iterable:
# largest_index = len(lst) - 1

for index, value in enumerate(lst):
	print(f'index: {index}, value: {value}')