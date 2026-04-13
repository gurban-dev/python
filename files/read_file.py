'''
To read data from a file, a Python program must follow this process:
1. Open the File

   Get the file path.

   Specify how you want to interact ("r") read mode.

2. Read the Content

   Have all of the content returned as one large string.
   .read() method

   Read line by line (one line at a time):
   for line in file:
       print(line)

3. Process the Data
   
   Strip the leading and trailing whitespace characters (line.strip())

   Split the value (line.split(","))

4. Close the File

   Release the system resources and prevent a file lock (multiple programs
   editing the same file simultaneously).

   file.close()
'''


# This program reads and displays the contents of the philosophers.txt
# file.
def main():
	'''
	The open() function opens the philosophers.txt,	file and returns
	a file object.

	A file object is an object that is associated with a specific file
	and provides a way for the program to work with that file.

	"file_obj" references the file object.

	This file object can be used to read data from the philosophers.txt
	file.

	'r' indicates that the file is opened only for reading. The
	file cannot be changed or written to.

	./ refers to the current directory that the Python program is
	located in. The current directory is where the Python program
	should look for the philosphers.txt file.

	./../ refers to the directory one level	above where the Python
	program is located.'''

	# Open a file named philosophers.txt.
	file_obj = open('./philosophers.txt', 'r')

	'''
	Question:
	Can the open() function open files of all extensions?

	Answer:
	The open() function can access any file that exists on the
	filesystem, regardless of its type or extension. What matters
	is how you read it:
	Text files: open in text mode ('r', 'w'), Python treats contents
	as strings.

	Binary files: open in binary mode ('rb', 'wb'), Python treats
	contents as bytes.
	'''

	'''
	If a file has been opened for reading (using the 'r' mode) you
	can use the file object's read() method to read its entire
	contents into memory. When you call the .read() method, it
	returns the file's contents as a string.'''
	file_contents = file_obj.read()

	# Print the data that was read into memory.
	print(f'file_contents:\n{file_contents}')

	# Close the file object.
	file_obj.close()

main()