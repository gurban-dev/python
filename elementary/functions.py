# Think of a function as a standalone reusable block of code.

# 'num1' and 'num2' are the parameters that the function
# accepts.
def sum(num1, num2):
  print('num1:', num1)
  print('num2:', num2)

  print(f'sum of {num1} and {num2}: {num1 + num2}')

# Find the sum of two numbers.
# Whenever you call a function in Python, remember
# that you will have a pair of parentheses right
# after the name of the function.

# The arguments you pass to the function are written
# in between the parentheses and separated by commas (,).
sum(1, 2)