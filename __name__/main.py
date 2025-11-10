import greet
from greet import say_hello

'''
When greet.py is imported, the __name__ variable inside
greet.py becomes "greet", so the code inside
if __name__ == "__main__": does not run.

When greet.py is run directly (python3 greet.py), the
__name__ variable becomes "__main__", and that block does
run.

Notice how just by importing the greet module, the
lines of source code or instructions written globally
are executed.

After the source code in greet.py is executed, the lines
in this file will follow suit.
'''

print("\nNow inside main.py\n")

# However, functions from greet.py can still be imported
# and invoked in this file.
say_hello()