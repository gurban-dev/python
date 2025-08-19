# This program reads and displays the
# contents of the philosophers.txt file.
def main():
  '''
  The open() function opens the philosophers.txt,
  file and returns a file object.

  A file object is an object that is associated
  with a specific file and provides a way for
  the program to work with that file.

  "infile" references a file object.

  This file object can be used to read data
  from the philosophers.txt file.

  'r' indicates that the file is opened only
  for reading. The file cannot be changed or
  written to.

  ./ refers to the current directory that
  the Python program is located in.

  ./../ refers to the directory one level
  above where the Python program is located.'''

  # Open a file named philosophers.txt.
  infile = open('philosophers.txt', 'r')

  '''
  If a file has been opened for reading (using
  the 'r' mode) you can use the file object's
  read method to read its entire contents into
  memory. When you call the read method, it
  returns the file's contents as a string.'''
  file_contents = infile.read()

  # Close the file object.
  infile.close()

  # Print the data that was read into
  # memory.
  print(f'file_contents:\n{file_contents}')

main()