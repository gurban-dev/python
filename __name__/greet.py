def say_hello():
  	print("\nHello!")

print("In greet.py:\nThis runs no matter what.\n")

# '__name__' is categorised as a dunder variable because
# it contains two leading and trailing underscores.
print('__name__:', __name__)

'''
When greet.py is imported in another file, the __name__
variable inside greet.py becomes "greet", so the code inside
if __name__ == "__main__": does not run.

When greet.py is run directly (python greet.py), the
__name__ variable becomes "__main__", and that block does
run.
'''
if __name__ == "__main__":
	print("\nRunning greet.py directly!")

	say_hello()

# Typically, an else wouldn't be written when __name__ is not
# equal to "__main__" because it's not necessary to explicitly
# print that a file is being imported.
else:
  	print("\ngreet.py is being imported as a module by another file.")