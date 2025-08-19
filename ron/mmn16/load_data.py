# "pandas" is a module.
# "pd" is an alias or an alternative name.
# The "as" keyword comes before the alias. 
import pandas as pd

def load_data(file_name):
  # The try except block will catch errors
  # gracefully. Gracefully meaning that the
  # error will not cause the program to crash.
  try:
    df = pd.read_csv(file_name)

    print('CSV file ')
  except FileNotFoundError:
    print('Error: The file was not found.\n'
          'Please check the file path and try again.')

  # Return the Pandas DataFrame back to
  # where this function was invoked.
  return df

load_data('./nasa.csv')