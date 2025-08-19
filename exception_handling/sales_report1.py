# This program displays the total of the
# amounts in the sales_data.txt file.

def main():
  # Initialize an accumulator.
  total = 0

  '''
  Any source code that may generate an exception
  should be put in the try block. This way, it
  is caught rather than crashing the entire
  program.'''
  try:
    '''
    Open the sales_data.txt file.
    If the file that the program is attempting to open
    is not found, the program will jump to the IOError
    except clause.
    
    The sales_data.txt file was opened for reading and
    a file object was returned.
    
    ./ tells Python to search for the file in the
    current directory.'''
    infile = open('./sales_data.txt', 'r')

    # If the sale_data.txt file was one directory
    # level above.
    # infile = open('./../sales_data.txt', 'r')

    # If the sale_data.txt file was one directory
    # level below.
    # infile = open('./sub_directory_name/sales_data.txt', 'r')

    # Read the values from the file and
    # accumulate them.
    for line in infile:
      print('type(line):', type(line))

      '''
      If the value being casted as a float, is not
      actually a numeric value, the program jumps
      from total += float(line) to the ValueError
      except clause.'''

      # total = total + float(line)
      total += float(line)

      '''
      If the program were to cast '50.00'
      as an integer, '50.00' would have to
      be cast as a float first before being
      cast as an integer.'''      
      # total += int(float(line))

    # Close the file.
    infile.close()

    # Print the total.
    # Notice that "total" is a float because
    # the numeric values were casted as floats
    # above with the float() function.
    # print('\n', format(total, ',.2f'))

    print('\ntotal:', total)

    # print('total:', total)
  except IOError:
    print('\nAn error occured trying to read the file.')
  except ValueError:
    print('\nNon-numeric data found in the file.')
  except:
    print('\nAn error occured.')

main()