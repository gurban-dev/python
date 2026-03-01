'''
A decorator is a function that takes another function as input
and returns a new function with modified behavior, without
changing the original function's code.

Use case:
Logging and debugging: Inspect function calls, arguments,
and return values without modifying the original function.
'''

# A three-layer function is the conventional approach
# for handling arguments in decorators.
def func(function):
	# The parameter 'function' is expected to be assigned
	# a function that was passed as an argument to this
	# func() function.

	# *args and **kwargs means that the function "f"
	# can accept any number of positional and keyword
	# arguments.
	def wrapper(*args, **kwargs):
		print(f"Function name: {function.__name__}")

		pos_args = ""

		# 'args' references a tuple.
		if args:
			pos_args = ", ".join(str(arg) for arg in args)

			print("Positional arguments:", pos_args)
		
		keyword_args = ""
		
		# 'kwargs' references a dictionary.
		if kwargs:
			keyword_args = ", ".join(
				f"{key}={value}" for key, value in kwargs.items()
			)

			print("Keyword arguments:", keyword_args, '\n')

		# return_val = sum(5, 6)
		return_val = function(*args, **kwargs)

		print('return_val:', return_val)

		print(f'\nThe invocation of {function.__name__} finished.\n')

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

print('func2():')
func2()

@func
def sum(num1, num2):
	print(f'num1: {num1}, num2: {num2}')

	return num1 + num2

# The same as:
# sum = func(sum)

print('sum(5, num2=6):\n')
total = sum(5, num2=6)

# print('total:', total)