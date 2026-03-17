# This program writes three
# lines of data to a file.
def main():
  '''
  If the philosophers.txt file doesn't exist,
  it will be created because of the 'w' mode.

  The philosophers.txt is created in the same
  directory as this program is located in.

  'w' indicates that Open a file for writing.
  If the file already exists, erase its
  contents.

  If a file with the specified name already
  exists when the file is opened, the contents
  of the existing file will be deleted.'''
  outfile = open('./philosophers.txt', 'w')

  '''
  In the format, file_variable is a variable
  that references a file object, and string
  is a string that will be written to the file.

  The file must be opened for writing (using
  the 'w' or 'a' mode).

  write() is a method because it belongs to an
  object. It is defined inside of Python's file
  object class.'''

  # Write the names of three
  # philosphers to the file.
  # outfile.write('John Locke\n')
  # outfile.write('David Hume\n')
  # outfile.write('Edmund Burke\n')

  # "philosophers" is an iterable meaning
  # that the program can iterate over the
  # elements it stores.
  philosophers = [
    'John Locke',
    'David Hume',
    'Edmund Burke'
  ]

  # On each iteration, the "philosopher" variable
  # will be assigned the current element.
  for philosopher in philosophers:
    print('philosopher:', philosopher)

    # 1st iteration:
    # philosopher + '\n'
    # 'John Locke' + '\n' -> 'John Locke\n'
    outfile.write(philosopher + '\n')

  '''
  Once a program finishes working with a file,
  it should close it to avoid data loss. This
  is because data is first written to a memory
  buffer before being saved to the file. If
  the file isn't closed, unsaved data in the
  buffer may not be written.

  Closing the file ensures all buffered data
  is properly saved and improves system
  performance.'''

  # Close the file.
  outfile.close()

main()