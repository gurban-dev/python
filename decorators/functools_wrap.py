from functools import wraps

'''
A decorator takes a function, wraps it inside another function
(the wrapper), and returns that wrapper, allowing additional
lines of code to be added before and after the source code in
the function being decorated. The behaviour of a function is
changed without having its code modified.
'''

def log_calls(func_being_wrapped):
	# @wraps(func_being_wrapped) preserves the metadata of the
	# function being decorated.
	@wraps(func_being_wrapped)
	def wrapper(*args, **kwargs):
		print(f"Calling {func_being_wrapped.__name__} with {args}, {kwargs}")

		result = func_being_wrapped(*args, **kwargs)

		print(f"\n{func_being_wrapped.__name__} returned {result}.")

		return result

	return wrapper

@log_calls
def greet(given_name: str, age=20):
	print(f'\nHello {given_name}! You are {age} years old.')

if __name__ == '__main__':
	greet('Alexander', age=25)

	# Comment and uncomment @wraps(func_being_wrapped) above to see
	# how the __name__ property of greet() is preserved with it.
	print('\ngreet.__name__:', greet.__name__)