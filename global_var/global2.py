# Create a global variable.
number = 0

def main():
  '''
  Tells the interpreter that the main function
  intends to assign a value to the global number
  variable. Without the subsequent line, the
  program wouldn't be able to modify the global
  variable called "number".'''
  global number

  number = int(input('Enter a number: '))

  # Since show_number() is being invoked locally
  # within another function, the actual function
  # can be declared below the invocation.
  show_number()

def show_number():
  print('\nThe number you entered is', number)

# Call the main function.
main()