'''
Code Reusability
Writing functions make it possible to write
source code that performs a particular task
and then reuse that code all throughout the
program. These are referred to as user-defined
functions.

If there aren't any names between the open and closed
parentheses, this indicates that the function does not
accept any parameters.

Syntax for a parameterless function:
def function_name():
  instruction_1

  instruction_2

  ...

  etc.

To invoke/call a declared function, type the
name of the function followed by a pair of open
and closed parentheses:

function_name()
'''

# Function without parameters.
# This is a void function because it returns None.

# The function say_hello() prints a message but does
# not send a value back to where it was invoked in the
# program.
def say_hello(no_of_orders: int) -> None:
  print("Hello, World!")

  total: int = 10 * no_of_orders

  print('total:', total)

  # Have the function return a value if you need to
  # access that value outside of the function.
  # return total

return_val: int | None = say_hello(5)

# Output:
# return_val: 50
print('\nreturn_val:', return_val)

'''
Parameters in a function definition are separated
by commas.

These parameters can be referenced inside of the
function's body which is where the instructions
are written.

Syntax for a parameterised function:
def function_name(parameter_1, parameter_2):
  instruction_1

  instruction_2

  ...

function_name(argument_1, argument_2)

When function_name() is invoked/called, argument_1
will be assigned to parameter_1 just as argument_2
will be assigned parameter_2.

argument_1 and argument_2 are being passed to
function_name().

function_name() is accepting parameter_1 and
parameter_2.
'''

'''
A parameter can be thought of as a piece of
data that a function will accept.

The add() function is accepting two pieces
of data called "first_num" and "second_num".

To determine where the data is coming from,
analyze the function call for add().

The value of the first argument which is "num1",
is assigned to the first parameter, "first_num".
'''

# Function with parameters.
def add(first_num: int, second_num: int) -> int:
  print('\nfirst_num + second_num:', first_num + second_num)

  # return first_num + second_num

# Two integer variables declared.
num1: int = 3
num2: int = 5

'''
Pass the arguments to the add() function.
It's important to note that the names of the
arguments do not have to be the same as the
parameter names that can be seen in the
function signature.

num1 will be assigned to parameter "first_num"
and num2 will be assigned to parameter
"second_num" because of the order that these
arguments were passed to the add() function
in.'''

# Output: 8
print('add(num1, num2):', add(num1, num2))

num1 = 1
num2 = 2
add(num1, num2)

# What does the subsequent line output in the
# terminal?
add(3, 5)

'''
The output "8" is not seen anymore in the
terminal because the function call add(3, 5)
is not inside of a print statement.

If nothing is printed out with print(), nothing
will be outputted to the terminal.'''