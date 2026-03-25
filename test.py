import sys

items_lst = [num for num in range(1_000)]

print(sys.getsizeof(items_lst))

items_gen_exp = (num for num in range(1_000))

print(sys.getsizeof(items_gen_exp))