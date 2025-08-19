'''
The "def" keyword indicates that a function has
been declared.

The name of the subsequent function is "message".

Open and closed parentheses as well as a colon
must follow the name of a declared function.'''
def message():
  '''
  Printing "I am Arthur,\nKing of the Britons"
  inside this function assigns a responsibility
  to this function.

  This is a more organised way of writing
  source code than calling print() in the main
  function.'''

  # print('I am Arthur,')
  # print('King of the Britons.')

  # Local variable because it is declared
  # inside of the message() function.
  entire_message = 'I am Arthur,\nKing of the Britons.'

  """
  If the following line is uncommented, this
  function is no longer a void function because
  it would be returning a value.
  
  A void function is one that doesn't return a value."""
  return entire_message
# This line is already outside of the function's
# body because it is not indented.

"""
This code defines a function named message.

The message() function contains a block with
three statements. Executing the function will
cause these statements to execute."""

"""
To execute a function, you must call it.
The below line is how we would call the
message() function.

Passing a void function to a print() function
will output None because the void function
returns nothing.
"""

'''
Without print(), nothing will be outputted
to the terminal.

The "msg" variable is being assigned the
value returned from the message() function.'''
msg = message()

# Displays the data type of the "msg" variable.
print('type(msg):', type(msg))

# The value returned from the function message()
# will be outputted to the terminal. The return
# value doesn't need to be assigned to a variable.
print('\nmessage():', message())

"""
Once all of the statements in a function are executed,
the interpreter jumps back to the part of the program
that called the function, and the program resumes
execution at that point (line 65 and 73 in this case)."""