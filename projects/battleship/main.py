# Constant
SHIP_LENGTH = 3
NUM_OF_SHIPS = 2


def coordinates_for_ship():
  # A "bow" is the front of a ship.

  # It serves as a placeholder when a statement
  # is syntactically required but no action is
  # desired or intended at that point in the code.
  pass

# def validate_inputted_coordinates(inputted_coordinates):
#   # Remember the parameter name doesn't need to be the
#   # same as the variable passed as an argument.

#   """Accepts inputs like 3,A."""

#   # The .strip() method removes the leading and trailing
#   # whitespace characters from a string.
#   inputted_coordinates = inputted_coordinates.strip()

#   # The separater is the comma in the user input.
#   sep = None

#   if ',' in inputted_coordinates:
#     sep = ','
  

# Suppose you had to print something in a Python program
# a hundred times.

# If the greeting changes, rather than changing the message
# in a hundred lines, you only need to modify it in one line.
def greet_travelers(language: str) -> None:
  # This greet_travelers() function is accepting "language"
  # as a parameter.

  # The "language" parameter is assigned the argument that
  # is passed to this function on a function call.

  # E.g.
  # In the case of greet_travelers('English'), 'English' is
  # the value that is assigned to the "language" parameter.

  if language == "English":
    print('Welcome to the international airport!')
  elif language == "German":
    print('Bienvenue à l\'aéroport international !')

greet_travelers('English')

greet_travelers('German')

# def input_coordinate(prompt):
#   """Prompt until the end user inputs a valid coordinate
#      within the board."""
#   while True:
#     # Column 3, Row A
#     # 3,A

#     coordinates = input('Input the coordinates for the ship\'s bow: '
#                         + f' (format: x, y with x between 1 and 10 and y between A and J): ')

#     validate_inputted_coordinates(coordinates)
#     # coordinates = input(prompt )

def coordinate_is_valid(column, coordinate):
  if column:
    # Checks that the end user inputted a number rather
    # than a non-numeric input.
    try:
      value = int(coordinate)
    except ValueError:
      print("Error: You must input a number from 1 to 10!")
      return False
    
    if 1 <= coordinate <= 10:
      return True
    else:
      return False
  else:
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    
    if coordinate in rows:
      return True
    else:
      print("Error: You must input a row option from A to J!")
      return False


def select_coordinates():
  while True:
    column_coordinate = input('From 1 to 10, choose a column to place the ship\'s bow: ')

    if coordinate_is_valid(True, column_coordinate):
      # Have the flow of the program exit the while loop.
      break
  
  while True:
    column_coordinate = input('From A to J, choose a row to place the ship\'s bow: ')

    if coordinate_is_valid(False, column_coordinate):
      # Have the flow of the program exit the while loop.
      break

# Entry point of the Python program.

select_coordinates()