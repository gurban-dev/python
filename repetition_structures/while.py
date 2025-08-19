# This program calculates sales commissions.

# Create a variable to control the loop.
keep_going = 'y'

# The "while" keyword is a prerequisite.

# Calculate a series of commissions.
while keep_going == 'y':
  # Get a salesperson's sales and commission rate.
  sales = float(input('Enter the amount of sales: '))

  comm_rate = float(input('Enter the commission rate: '))

  # Calculate the commission.
  commission = sales * comm_rate

  # Display the commission.
  print('\nThe commission is $',
        format(commission, ',.2f'), sep='')

  '''
  The format specifier ',.2f' in Python is used to
  format floating-point numbers for clearer readability.

  A breakdown of ',.2f':

  , → Adds commas as thousands separators.
  Example: 1234567.89 → 1,234,567.89

  .2f → Formats the number as a floating point
  with 2 digits after the decimal point.
  Example: 45.6789 → 45.68
  '''

  # See if the user wants to input another pair
  # of values for sales and commission rate.

  # Typing nothing and simply clicking the "Enter"
  # button on the keyboard inputs an empty string
  # literal. The while loop will terminate after
  # this.
  keep_going = input('\nDo you want to calculate another ' +
  'commission (Enter y for yes): ')

  # So long as the following condition evaluates to
  # True, the while loop will continue iterating:
  # keep_going == 'y'
  print('\nkeep_going == \'y\':', keep_going == 'y', '\n')