# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# The "while" keyword is a prerequisite.

# Calculate a series of commissions.
while keep_going == 'y':
  # Get a salesperson's sales and commission rate.
  sales = float(input('Enter the amount of sales: '))

	# Python's built-in input() function returns a string.

  # In this case, that string must be converted to a
  # float data type because of the multiplication that
  # follows.
  comm_rate = float(input('Enter the commission rate: '))

  # In Python, multiplying an integer by a float will
  # compute to be a float.

  # Calculate the commission.
  commission = sales * comm_rate

  print(f'\ncommission: {commission}')

  # Syntax:
  # format(float, format_specifier)

  # The comma in the format specifier inserts a
  # comma after every three digits.

  # The .2 means that only two digits after the
  # decimal point will be shown.

  # The f in the format specifier signifies that a
  # float is being formatted.

  # Display the commission.
  print('\nThe commission is $',
        format(commission, ',.2f'), sep='')

  '''
  The format specifier ',.2f' in Python is used to
  format floating-point numbers for clearer readability.

  A breakdown of ',.2f':

  , -> Adds commas as thousands separators.
  Example: 1234567.89 -> 1,234,567.89

  .2f -> Formats the number as a floating point
  with 2 digits after the decimal point.
  Example: 45.6789 -> 45.68
  '''

  # See if the user wants to input another pair
  # of values for sales and commission rate.

  # Typing nothing and simply clicking the "Enter"
  # button on the keyboard inputs an empty string
  # literal. The while loop will terminate after
  # this.
  keep_going = input('\nDo you want to calculate another ' +
                     'commission (Enter y for yes): ').lower()

  # So long as the following condition evaluates to
  # True, the while loop will continue iterating:
  # keep_going == 'y'
  print('\nkeep_going == \'y\':', keep_going == 'y', '\n')

# This is located outside of the while loop because the indentation
# level begins at the very beginning of the line.
print('The program has finished.')