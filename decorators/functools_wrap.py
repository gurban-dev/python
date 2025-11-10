from functools import wraps

'''
A decorator takes a function, wraps it inside another function
(the wrapper), and returns that wrapper, allowing additional
lines of code to be added before and after the source code in
the function being decorated. The behaviour of a function is
changed without modifying its own code.
'''

def log_calls(func):
  # @wraps(func) preserves the metadata of the function being
  # decorated.
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__} with {args}, {kwargs}")

    result = func(*args, **kwargs)

    print(f"\n{func.__name__} returned {result}.")

    return result

  return wrapper

@log_calls
def greet(given_name: str, age=20):
  print(f'\nHello {given_name}! You are {age} years old.')

if __name__ == '__main__':
  greet('Alexander', age=25)

  # Comment and uncomment @wraps(func) above to see how
  # the __name__ property of greet() is preserved with it.
  print('\ngreet.__name__:', greet.__name__)