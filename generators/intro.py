# An iterator makes it possible to loop through
# a sequence of some data without having to store
# the data in memory.

# range(1, 11) returns an iterable which is an object
# that can return an iterator using iter().
for i in range(1, 11):
	print(i)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map(lambda i: i**2, numbers)

print('\ny:', y)

print('\nnext(y):', next(y))
print('next(y):', next(y))

# __next__ is a dunder method.
print('y.__next__():', y.__next__())

print('\nFor loop begins')
for i in y:
	print(i)
print('')

# Python's built-in range() function returns an iterable.
iterable = range(1, 11)

for i in iterable:
  print('i:', i)

# To access the elements inside of the iterable, the
# .__iter__() dunder method or iter() function can be
# utilised. Either one of these will return an iterator.
iterator = iterable.__iter__()

iterator = iter(iterable)

print('\niterator:', iterator)

# Access the element that the iterator points to can be
# done with .__next__() method or the next() function.
print('\niterator.__next__():', iterator.__next__())

print('\nGenerator')
def gen(num):
	for i in range(num):
		yield i

for i in gen(5):
	print(i)

print('\nManual Generator')

# A manual implementation:
def manual_gen():
	yield 0
	print('Pause 1\n')

	yield 1
	print('Pause 2\n')
	
	yield 2
	print('Pause 3\n')

	yield 3
	print('Pause 4\n')

	yield 4
	print('Pause 5\n')

x = manual_gen()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

one_trillion = 1000000000000

'''
range(one_trillion) does not create a list of a trillion
numbers in memory.

Instead, it stores only the start, stop, and step values
internally.
'''

# for i in range(one_trillion):
# 	pass

'''
yield makes the following a generator function.

When generator() is invoked, it does not execute the loop
immediately.

Instead, it returns a generator object that produces numbers
one at a time when requested. A generator object is an iterator.

From the perspective of memory storage, this is extremely efficient
since only one number exists in memory at a time.
'''
def generator(num):
	for i in range(num):
		yield i

		print(f'Pause {i}')

generator_obj = generator(one_trillion)

print('\nnext(generator_obj):', next(generator_obj))

# Outputs 0, 1, 2, ... N-1
# for num in generator_obj:
# 	print('num:', num)

'''
Use case of a generator:
Loop through a large amount of data without needing to store
all of it.

You do not care about the data before or after the current
iteration. You only care about the current iteration.

Examples:
Print out all of the numbers in a sequence. Only the current
number must be known.

Determine if a word exists in a file containing billions of
lines. You only need to know the content written on the current
line. One row would be yielded at a time this way a few bytes
of memory would be occupied rather than reading the file and
occupying gigabytes of memory.
'''