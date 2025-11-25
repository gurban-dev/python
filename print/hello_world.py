'''
Python has a built-in function named print().

This function accepts an argument and prints it
to the screen.

The open and closed parentheses pair () tells
us that we are working with a function.

"Hello World!" is a string literal and it is being
passed as an argument to the print() function.

How is it known that "Hello World!" is a string literal?
Answer: The quotation marks are hardcoded into the source code.
'''
print("Hello World!")

'''
The print() function has a parameter named "end".
The "end" parameter is implicitly or internally passed a
newline escape sequence ("\n") by default.

For this reason, the print() function by default has a
newline escape sequence at the end of its output:
"Hello World!\n"
'''

# This default behaviour of the print() function can be altered.
print("Hello World!", end="")

'''
"Hello World!" is a positional argument because the
name of the parameter is not explicitly written out.

end="" is a keyword argument because the name of the
parameter "end" is explicitly written out.

"end" is the name of a parameter in the print() function:
https://docs.python.org/3/library/functions.html#print

Passing an empty string ("") to the "end" parameter removes
this default behaviour:
"Hello World!"
'''

'''
Whenever new source code in a Python file is written, the file
must be saved. The file can be automatically saved by enabling
the "Auto Save" option in Visual Studio Code after clicking the
"File" button at the top left.

Once the Python file has been saved, the program can be run by
clicking on what looks like a "play" button at the top right of
the Visual Studio Code window, or by executing the following
command in the terminal:
python3 <name_of_file>.py

In this case, the following command should be executed:
python3 hello_world.py

A command is executed by clicking the "Enter" button on the
keyboard.
'''

# The print() function on the next line is being
# passed two positional arguments:
# 1st argument: '2 + 2:'
# 2nd argument: 2 + 2

# The 1st argument '2 + 2:' is a string literal because
# it is surrounded by quotation marks.
# The 2nd argument 2 + 2 will perform an arithmetic operation.
print('2 + 2:', 2 + 2)

print("'2' + '2':", '2' + '2')

'''
Putting a newline escape sequence at the beginning of the
print statement is merely to demonstrate that a newline
can be included at beginning of the output.

Inserting a newline escape sequence after "of" and before
"this" makes the output more readable.
'''
print('\nThere is a newline character at the beginning of\n'
      'this string and an automatically included one at\n'
      'the end.')

'''
Does the print() function have a character limit?

Answer:
The print() function in Python itself doesn't have
a strict character limit.

If you try to print an extremely large string (e.g.,
gigabytes of data), your computer might encounter
memory issues.

However, this would be more of a memory error rather
than a strict character limit for the print() function.'''

# E.g. Repeating a character by a billion times and then
#      attempting to print it to the screen.
# print('*' * 1_000_000_000)