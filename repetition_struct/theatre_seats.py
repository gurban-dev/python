'''
Integers num_rows and num_columns are read
from input representing the number of rows
and columns of a theater's seating plan.

Complete the nested for loop to output each
seat label, as shown in the example. Each
seat label is followed by a space, and each
row is followed by a newline.
'''

def prompt_integer_input(prompt_msg):
  while True:
    # try:
    #   number = int(input(prompt_msg))

    #   # Send the value of the "number" variable
    #   # back to where this function/method was
    #   # invoked.
    #   return number
    # except ValueError:
    #   print("\nInvalid integer! Please enter a valid integer.\n")

    '''
    If you don't want to use a try except block,
    integer input validation can also be
    implemented with the following.

    If the string inputted by the end user is not
    numeric, then the input can't possibly be
    casted as an integer.'''
    numberStr = input(prompt_msg)

    if not numberStr.isnumeric():
      print("\nInvalid integer! Please enter a valid integer.\n")
    else:
      return int(numberStr)


num_columns = prompt_integer_input('Input the number of columns in the theatre: ')

print('')

num_rows = prompt_integer_input('Input the number of rows in the theatre: ')

# Start with 'A' as the first column letter.
current_column_letter = 'A'

print('')

for current_row in range(num_rows):
  for current_column in range(1, num_columns + 1):
    '''
    end=' ' passed as the second argument to the
    print() function replaces the automatically inserted
    newline escape character at the end of the output,
    with a whitespace character (' ').'''
    print(f'{current_column}{current_column_letter}', end=' ')

  # Can be commented out as it is merely to
  # gain a deeper level of understanding.
#   print(f'''\n
# current_column_letter: {current_column_letter}
# ord({current_column_letter}): {ord(current_column_letter)}
# chr({current_column_letter} + 1): {chr(ord(current_column_letter) + 1)}''')

  '''
  The ord() function returns the number representing
  the unicode code of a specified character.
  67 is the unicode for character C.

  The chr() function returns the character that
  represents the specified unicode.

  ord(current_column_letter) returns the unicode of the
  letter representing the current column and chr()
  returns the character repesenting the value of that
  unicode plus 1.

  This is merely a way to get the next letter in the
  alphabet.
  '''
  current_column_letter = chr(ord(current_column_letter) + 1)

  print('\n')