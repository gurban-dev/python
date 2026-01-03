'''
add() is a user-defined function.

Parameters are the variables listed inside the
parentheses in a function header.

They act as placeholders for the arguments that will
be passed to the function.

Arguments are the actual values passed to a function
when it is called. These values are assigned to the
parameters defined in the function header.'''

# "first_num" and "second_num" are parameters.
def add(
  first_num: int | float,
  second_num: int | float) -> int | float:

  print('first_num:', first_num)
  print('second_num:', second_num, '\n')

  # Send the sum of first_num and second_num
  # back to where the add() function was
  # invoked in this program.
  return first_num + second_num

# 5 and 6 are arguments.
sum1: int = add(5, 6)

print(f'sum of 5 and 6: {sum1}\n')

sum2: float = add(5.0, 6.0)

print(f'sum of 5.0 and 6.0: {sum2}\n')

num1: int = 2
num2: float = 2.0

'''
The parameter names do not have to match the names
of the variables passed as arguments to the function.

Notice how instead of assigning the return value
of the function call, the function call can occur
in an actual print statement.

Since 2 is being added with 2.0, the return value
is a floating point number rather than an integer.

In Python, the sum as well as the product of an
integer and float is always a float.'''
print(f'add(num1, num2): {add(num1, num2)}')