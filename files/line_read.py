'''
In Python, you can use the readline method to
read a line from a file.

A line is simply a string of characters that
are terminated with a \n (newline escape
sequence).

The method returns the line as a string,
including the \n.'''

# This program reads the contents of the
# philosophers.txt file one line at a time.
def main():
  # Open a file named philosophers.txt.
  infile = open('./philosophers.txt', 'r')

  # Read three lines from the file.
  line1 = infile.readline()
  line2 = infile.readline()
  line3 = infile.readline()

  # Close the file.
  infile.close()

  # Print the data that was read
  # into memory.
  print('line1:', line1)
  print('line2:', line2)
  print('line3:', line3)

  '''
  The blank line displayed after each line in
  the output. This is because each item that
  is read from the file ends with a newline
  character ( \n ).'''

main()