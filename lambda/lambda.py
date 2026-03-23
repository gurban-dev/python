'''
Lambda functions are defined without a name.

Use them for short tasks where defining an entire function
would be unnecessarily verbose or writing more source code
than needed.

Syntax:
lambda parameter(s): expression
'''

# Lambda function where one argument is passed.
add_ten = lambda num: num + 10

# Equivalent:
def add_ten(num: int) -> int:
    return num + 10

# The argument 10 is being assigned to the parameter 'num'.
print('add_ten(10):', add_ten(10))

# Lambda function where two arguments are passed.
multiply = lambda num1, num2: num1 * num2

print('multiply(10, 10):', multiply(10, 10))