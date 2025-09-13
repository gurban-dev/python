import functools

def debug(func):
  """Print the function signature and return value"""
  @functools.wraps(func)
  def wrapper_debug(*args, **kwargs):
    # repr() is a Python built-in function that returns a string
    # representation of an object meant to be unambiguous and,
    # ideally, could be used to recreate the object.

    # Simply put, passing a string object to repr() will
    # return its value with the enclosed quotation marks.

    # It differs from str(), which is designed to be readable for humans.
    args_repr = [repr(a) for a in args]

    print('args:', args)

    # Output: Alexander
    print('\nargs[0]:', args[0])

    # Output: 'Alexander'
    print('repr(args[0]):', repr(args[0]))

    print('\nkwargs:', kwargs, '\n')

    kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]

    signature = ", ".join(args_repr + kwargs_repr)

    print(f"Calling {func.__name__}({signature})")

    value = func(*args, **kwargs)

    print(f"{func.__name__}() returned {repr(value)}")

    return value
  return wrapper_debug

@debug
def make_greeting(name, age=None):
  if age is None:
    return f"Hello {name}!"
  else:
    return f"Whoa {name}! {age} already, you're growing up!"
  
make_greeting('Alexander', age=20)