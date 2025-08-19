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
  def wrapper(*args, **kwargs) -> None:
    print('Started')

    returnVal = f(*args, **kwargs)

    print('Ended\n')

    return returnVal

  # Calls wrapper immediately and returns its
  # return value
  # return wrapper()

  # Returns the function object which is a reference to
  # the wrapper() function in this case that is stored
  # in memory.

  # Remember that functions are first-class objects, so
  # they can be assigned to variables.
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

print('func2():')
func2()

func3(5, 6)

x = func3(5, 6)

print('x:', x)