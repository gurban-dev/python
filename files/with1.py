# Since os is a built-in library module, it
# doesn't need to be installed with pip.
import os

# The time module it makes it possible to pause the execution
# of the Python program.
import time

file_name = "notes.txt"

'''
When used with a with statement, the open() function acts as a
context manager.

It calls the file object's __enter__() method when entering the
block (opening the file) and __exit__() when leaving it (closing
the file).

The with open("notes.txt") as f: statement:
1. Calls open("notes.txt").
2. Assigns the resulting file object to the variable file_object.

When the program exits the block, the file is automatically closed,
releasing system resources such as file handles and memory buffers.

The second argument "w", instructs Python to open this file for writing.
With "w", if the file doesn't already exist, the Python program will be
created.

If the same file already exists, writing to it will erase everything in
it.
'''

# Create a sample file.

# "w" represents write mode (this program will write data to the file).
with open(file_name, "w") as file_object:
	file_object.write("First line\nSecond line\nThird line   ")

# Read the file.

# "r" represents read mode (this program will read data from the file).
with open(file_name, "r") as file_object:
	contents = file_object.read()

print("contents:\n", contents)

new_lines = ["Fourth line", "Fifth line"]

# Opening the file to append new data.

# If you want to keep the exisitng data and add to it, use "a"
# as opposed to "w" which will erase the existing data.
with open(file_name, "a") as file_obj:
	for line in new_lines:
		# file_obj.write("\n" + line)

		'''
		When a file is opened in append mode, the file pointer is
		automatically positioned at the end of the file. This ensures
		that any new data written to the file is added after the
		existing content, without overwriting it.
		'''
		file_obj.write(line + "\n")

print('\nReading the file line by line:')
with open(file_name, "r") as file_obj:
	# Reading the file line by line.
	for line in file_obj:
		# Remove the leading and trailing whitespace characters
		# using the .strip() method.
		print("line.strip():", line.strip())

# with open(...) automatically closes the file when done.

# "r" = read mode, "w" = write mode (overwrites file), "a" = append mode.

# Pause the execution of the program for three seconds to open the
# notes.txt file and see the content that was written to it.
print('\nProgram paused for 5 seconds...')

time.sleep(5)

# os.getcwd() will return the current working directory.
# print('os.getcwd():', os.getcwd())

entire_file_path = os.getcwd() + '/notes.txt'

print('\nentire_file_path:', entire_file_path)

# Deletes the notes.txt file.
if os.path.exists(file_name):
  	os.remove(file_name)