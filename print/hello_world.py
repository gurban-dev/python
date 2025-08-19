'''
The following is the print() function.

The open and closed parentheses pair tells
us that we are working with a function.

"Hello World!" is a string literal and it is
being passed to the print() function.

() indicate that a function is being invoked/called.

Two arguments are being passed to the print()
function on the next line:
"Hello World!"
""

print() automatically inserts a newline escape
sequence at the end of its output.
"Hello World!\n

This automatic newline character can be
removed by assigning "" (an empty string)
to the end parameter inside the print()
function.

Passing an empty string ("") as an argument to
the end parameter removes this default behaviour:
"Hello World!"

Be sure to save the changes you make in
the file/program you are working on.'''
print("Hello World!", end="")

# After writing source code in a Python file,
# the file must be saved.

# Once the Python file has been saved, we can
# now run the program by executing the following
# command in the terminal:
# python3 <name_of_file>.py

# In this case, the following command
# should be executed:
# python3 hello_world.py

# A command is executed by clicking
# the "Enter" key on the keyboard.
print('Good morning!')

# Using two lines two write a print statement
# does not add another newline escape sequence.
print('There is a newline character at the '
      'beginning of this string and an '
      'automatically included one at the end.')

'''
Putting a newline escape sequence at the
beginning of the print statement is merely to
demonstrate that a newline can be included
at beginning of a print statement.

Inserting a newline escape sequence after "of"
and before "this" makes the output more readable.
'''
print('\nThere is a newline character at '
      'the beginning of\nthis string and '
      'an automatically included one at\nthe end.')

# Does the print() function have a character limit?
'''
The print() function in Python itself doesn't have
a strict character limit.

If you try to print an extremely large string (e.g.,
gigabytes of data), you may run into memory issues.

However, this would be more of a memory error rather
than a strict character limit for the print() function.'''