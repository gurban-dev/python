'''
add() is a user-defined function.

Parameters are the variables listed inside the
parentheses in a function header.

They act as placeholders for the argument that
will be passed to the function.

Arguments are the actual values passed to a function
when it is called. These values are assigned to the
parameters defined in the function header.'''

# "first_num" and "second_num" are parameters.
def add(first_num, second_num):
  print('first_num:', first_num)
  print('second_num:', second_num, '\n')

  # Send the sum of first_num and second_num
  # back to where the add() function was
  # invoked in the program.
  return first_num + second_num

# 5 and 6 are arguments.
sum1 = add(5, 6)
sum2 = add(5.0, 6.0)

print(f'sum of 5 and 6: {sum1}\n')
print(f'sum of 5.0 and 6.0: {sum2}\n')

num1 = 2.5
num2 = 2.5

'''
The parameter names don't have to match the names
of the variables passed as arguments to the function.

Notice how instead of assigning the return value
of the function call, the function call can occur
in an actual print statement.

Since 2.5 was assigned to each of the variables
passed as arguments, the return value is a
floating point number rather than an integer.'''
print(f'add(num1, num2): {add(num1, num2)}')