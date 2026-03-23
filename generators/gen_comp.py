# A generator is a specific kind of iterator that is defined
# with yield. It automatically implements the .__iter__() and
# .__next__() dunder methods.

# Generator comprehension.
# Lazy evaluation: values are produced on-the-fly as you iterate,
# not all at once, saving memory. A generator remembers where it
# left off in the sequence.
generator_obj = (i for i in range(100))

# List comprehension.
lst = [i for i in range(100)]

print('type(generator_obj):', type(generator_obj), '\n')

print('generator_obj.__next__():', generator_obj.__next__(), '\n')

# Iterate through the generator object without using "yield".
# The for loop implicitly or internally calls the next() function
# on the generator object.
for num in generator_obj:
	if num != 9:
		print('num:', num, end=', ')
	else:
		print('num:', num)

# This for loop uses the same memory space as the generator
# expression below.
print('\nfor i in range(100):')
for i in range(100):
  	print('i:', i, end=' ')
print()

# Returns a generator object because of the "yield" keyword.
def gen():
	for i in range(100):

		# yield pauses the function, sends the value of 'i' back
		# to where this function was invoked and can resume later
		# on from where the generator left off in the sequence.
		yield i

generator = gen()

# The iter() function returns an iterator for the argument passed
# to it.
# print('\niter(generator):', iter(generator))

print('\nnext(generator):', next(generator))

print('\nnext(generator):', next(generator))

print('\nnext(generator):', next(generator))