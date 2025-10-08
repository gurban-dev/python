'''
A decorator is a function that makes it possible to modify
the behaviour of another function without changing that
function's actual code.
'''

# A three-layer function is the conventional approach
# for handling arguments in decorators.
def func(f):
  # *args and **kwargs means that the function "f"
  # can accept any number of positional and keyword
  # arguments.
  def wrapper(*args, **kwargs):
    print('Started')

    # Invokes func3(5, 6).
    return_val = f(*args, **kwargs)

    print('return_val:', return_val)

    print('Ended\n')

    return return_val

  # Calls wrapper immediately and returns its
  # return value
  # return wrapper()

  # Returns the function object which is a reference to
  # the wrapper() function in this case that is stored
  # in memory.

  # Remember that functions are first-class objects, so
  # they can be assigned to variables.

  # If you don't return anything, then the decorator has
  # nothing to replace the original function with so the
  # decorated function name (func2) gets overwritten with
  # None.
  return wrapper

# func2() is being decorated with @func.
@func
def func2():
  print('I am func2.')

# Produces the same outcome as putting the @func
# decorator on the line above the func2() function.
# func2 = func(func2)

@func
def func3(num1, num2):
  print('I am func3.')

  print(f'num1: {num1}, num2: {num2}')

  return num2

# The same as:
# func3 = func(func3)

print('func2():')
func2()

print('func3(5, 6):')
func3(5, 6)

x = func3(5, 6)

print('x:', x)