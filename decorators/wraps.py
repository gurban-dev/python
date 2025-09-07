import functools

# Decorator function.
def do_twice(func):
  # The @functools.wraps decorator preserves metadata about
  # the original function (attributes like __name__ along with
  # its memory address).

  @functools.wraps(func)
  def wrapper_do_twice(*args, **kwargs):
    func(*args, **kwargs)

    return func(*args, **kwargs)

  return wrapper_do_twice

@do_twice
def say_whee(num):
  print("Whee!")

  print(num)

# Function's memory address
print('say_whee:', say_whee)

# Function's name
print('say_whee.__name__: ' + say_whee.__name__ + '\n')

say_whee(10)

@do_twice
def return_greeting(name):
  print("Creating greeting")
  return f"Hi {name}"

# func(*args, **kwargs) is invoked twice in the
# wrapper_do_twice() wrapper function.

# However, return value "Hi {name}" is only printed
# once because the return value of the first invocation
# is not sent back to where the return_greeting() function
# was invoked (line 43).
hi_adam = return_greeting("Adam")

print(f'\nhi_adam: {hi_adam}')