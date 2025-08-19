import functools

# @functools.cache writes a custom cache and
# automatically resizes the cache.

# This is ideal when calling the same function
# repeatedly with the same arguments.

# To see the difference in the time duration, run this
# program with the following line commented and
# uncommented:
# @functools.cache
def fibonacci(n):
  if n < 2:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive call stack:
# 1, 1, 2, 3, 5, 8, 13, ...

# The pattern is that after the first and second
# 1s, the subsequent numbers are the sum of the
# previous ones.
# 2 is the sum of 1 and 1.
# 3 is the sum of 1 and 2.
# 5 is the sum of 2 and 3.

print(fibonacci(40))