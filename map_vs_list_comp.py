from typing import Any

# List comprehensions create a full list in memory, so they use
# more memory.

# In Python 3, the map() function is lazy, so it uses less memory
# because it computes values only when needed.

# Syntax:
# <expression> for <variable> in <iterable>

# A list comprehension iterates through an iterable and evaluates the
# expression for each item, inserting the result into a new list "nums".

# Any is a special type in Python's typing module that indicates a value
# can be of any type.
# nums: list[list[Any]] = [[] for _ in range(10)]

# Comment out the above line and uncomment the below to see
# the difference.
nums: list[int] = [num for num in range(10)]

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# The above list comprehension causes "nums" to be
# populated with the same elements as the below for
# loop.
# nums: list[int] = []
# for num in range(10):
#    nums.append(num)

print("nums:", nums)

def product_of_self(num: int) -> int:
  # return num * num
  return num**2

# for num in nums:
#   product_of_self(num)

# Syntax:
# map(function, iterable)
# nums = list(map(product_of_self, nums))

# lambda is an anonymous function written without "def".
# Use cases:
# A function only needs to be used once.
# The function is short.
# The function is called inside of another function
# like map().
# nums = list(map(lambda num: num ** 2, nums))

square = lambda num: num ** 2

# map() produces an iterator that computes items on-demand, not a list.
# The list is only realized if you explicitly convert it.

# This saves memory consumption.

nums = map(square, nums)

# Printing nums after nums = map(square, nums) will not show the
# squared numbers directly; it will show <map object at ...>.

# To see the numbers, you need print(list(nums)).

print('nums:', nums)