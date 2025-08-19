'''
A global variable is accessible to all
the functions in a program file.

When a variable is created by an assignment
statement that is written outside all the
functions in a program file, the variable
is global.'''

# Create a global variable.
my_value = 10

# The show_value function prints
# the value of the global variable.
def show_value():
  print('my_value:', my_value)

# Call the show_value function.
show_value()

'''
Most programmers agree that you should restrict
the use of global variables, or not use them at
all.

Global variables make debugging difficult. Any
statement in a program file can change the value
of a global variable. If you find that the wrong
value is being stored in a global variable, you
have to track down every statement that accesses
it to determine where the bad value is coming from.
In a program with thousands of lines of code, this
can be difficult.

In most cases, you should create variables locally
and pass them as arguments to the functions that
need to access them.'''