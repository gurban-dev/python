'''
Lambda functions are defined without a name.

Use them for short tasks where defining an
entire function would be unnecessarily
verbose or writing more source code than
needed.

Syntax:
lambda argument(s): expression
'''

# Lambda function where one argument is
# passed.
add_ten = lambda num: num + 10

print('add_ten(10):', add_ten(10))

# Lambda function where two arguments are
# passed.
multiply = lambda num1, num2: num1 * num2

print('multiply(10, 10):', multiply(10, 10))