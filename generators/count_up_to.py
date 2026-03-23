def count_up_to(num: int):
	count: int = 1

	# How many times do you think the count_up_to(5) function is
    # invoked? Uncomment the following line to see.
    # print("count:", count)

	while count <= num:
		# Pauses the function and returns the value of count.

		# The variable that is yielded remembers what the last
		# value that it referenced.
		yield count

		count += 1

for num in count_up_to(5):
	print('num:', num)

# A generator is a specific kind of iterator defined with yield.
# It automatically implements .__iter__() and .__next__().
gen_iterator = count_up_to(5)

# Dunder methods (two leading and trailing underscores).
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())
# print('gen_iterator.__next__():', gen_iterator.__next__())

# Python's built-in next() function.
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))
# print('next(gen_iterator):', next(gen_iterator))

# print('\ngen_iterator.__iter__():', gen_iterator.__iter__())