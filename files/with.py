# Since os is a built-in library module, it
# doesn't need to be installed with pip.
import os
import time

file_name = "notes.txt"

# Create a sample file.
with open(file_name, "w") as f:
  f.write("First line\nSecond line\nThird line")

'''
When used with a with statement, the open() function
acts as a context manager.

It calls the file object's __enter__() method when
entering the block (opening the file) and __exit__()
when leaving it (closing the file).

The file_object part assigns the opened file object to
file_object.

When the program exits the block, the file is automatically
closed, releasing system resources such as file handles and
memory buffers.
'''

# Read the file.
with open(file_name, "r") as file_object:
  contents = file_object.read()

print(contents)

new_lines = ["Fourth line", "Fifth line"]

# Opening the file to append new data.
with open(file_name, "a") as f:
  for line in new_lines:
    # f.write("\n" + line)

    '''
    When a file is opened in append mode, the
    file pointer is automatically positioned at
    the end of the file. This ensures that any
    new data written to the file is added after
    the existing content, without overwriting it.
    '''
    f.write(line + "\n")

print('\nReading the file line by line:')
with open(file_name, "r") as f:
  # Reading the file line by line.
  for line in f:
    print(line.strip())

# with open(...) automatically closes the file when done.

# "r" = read mode, "w" = write mode (overwrites file), "a" = append mode.

print('\nProgram paused for 3 seconds...')

time.sleep(3)

# print('os.getcwd():', os.getcwd())

entire_file_path = os.getcwd() + '/notes.txt'

print('\nentire_file_path:', entire_file_path)

if os.path.exists(file_name):
  os.remove(file_name)