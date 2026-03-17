# Import Python's built-in "re" module
# for utilising regular expressions.
import re

file_path = input('Enter the path of the Python file you \
\nwish to remove the line numbers from: ')

'''
E.g.

Before:
1 print('Good morning!')

After:
print('Good morning!')
'''

'''
The open() function creates a file object and associates
it with a file on the disk.

file_variable = open(filename, mode)

file_variable is the name of the variable that will
reference the file object.

filename is a string specifying the name of the file.

mode is a string specifying the mode (reading, writing, etc.)
in which the file will be opened.

It has two parameter values:
"file" which is the path and name of the file to open.
"mode" which is a string that defines which mode you want
to open the file in.
'''

try:
  # Open the file in read mode.
  with open(file_path, 'r') as file_object:
    lines = file_object.readlines()

  # Replace the first occurrence of digits followed
  # by a decimal point in each line.
  for i in range(len(lines)):
    lines[i] = re.sub(r'\d+\.', '', lines[i], count=1)

  # Open the file in write mode to overwrite the content.
  with open(file_path, 'w') as file_object:
    file_object.writelines(lines)
except FileNotFoundError:
  print(f"Error: The file '{file_path}' does not exist.")
except IOError as error:
  print(f"An I/O error occurred: {error}")