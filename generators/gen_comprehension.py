# Generator comprehension.
# Lazy evaluation: values are produced on-the-fly as you iterate,
# not all at once.
generator_obj = (i for i in range(10))

print('generator_obj:', generator_obj, '\n')

# List comprehension.
lst = [i for i in range(1_000)]

# Unlike the list comprehension above, this for loop uses the
# same memory space as the generator expression below.
for i in range(1_000):
  print('i:', i, end=' ')

# Returns a generator object because of the "yield" keyword.
def gen():
  for i in range(1_000):
    yield i

generator = gen()

print('\nnext(generator):', next(generator))

print('\nnext(generator):', next(generator))

# Iterate through the generator object without using "yield".
for num in generator_obj:
  if num != 9:
    print('num:', num, end=', ')
  else:
    print('num:', num)