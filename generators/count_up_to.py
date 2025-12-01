def count_up_to(num: int):
  count: int = 1

  while count <= num:
    # Pauses the function and returns the value of count.
    yield count

    count += 1

for num in count_up_to(5):
  print('num:', num)

# A generator is a specific kind of iterator defined with yield.
# It automatically implements .__iter__() and .__next__().
gen_iterator = count_up_to(5)

# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())

# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))

# print('\ngen_iterator.__iter__():', gen_iterator.__iter__())