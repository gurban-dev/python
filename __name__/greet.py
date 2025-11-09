def say_hello():
  print("Hello!")

print("This runs no matter what.\n")

print('__name__:', __name__)

'''
When greet.py is imported, the __name__ variable inside
greet.py becomes "greet", so the code inside
if __name__ == "__main__": does not run.

When greet.py is run directly (python3 greet.py), the
__name__ variable becomes "__main__", and that block does
run.
'''

if __name__ == "__main__":
  print("Running greet.py directly!\n")

  say_hello()