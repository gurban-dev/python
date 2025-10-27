import random
computer_row = random.randint(1, 10)
computer_column = random.randint(1, 10)

SHIP_LENGTH = 3
NUM_OF_SHIPS = 2
BOARD_MIN = 1
BOARD_MAX = 10

def coordinates_for_ship():
  pass

def coordinate_is_valid(column_or_row):
  try:
    value = int(column_or_row)
  except ValueError:
    print("Error: You must input a number from 1 to 10!")
    return False

  if 1 <= column_or_row <= 10:
    return True
  else:
    return False

def computer_places_ships():
  return [computer_column, computer_row]
bow_coordinates = []

def human_places_ships():
  while True:
  column_no = input('From 1 to 10, choose a column to place the ship\'s bow: ')

  if coordinate_is_valid(column_no):
    # Have the flow of the program exit the while loop.
    break

  while True:
    row_no = input('From 1 to 10, choose a row to place the ship\'s bow: ')
    if coordinate_is_valid(row_no):
      # Have the flow of the program exit the while loop.
      break

  get_human_orientation(row_no,column_no)
  return [column_no, row_no]

bow_coordinates = []
# Entry point of the Python program.

def validate_orientation_pos(row_no, col_no, orientation):
  if orientation == "s" and row_no < 3:
  print('The row number must be at least 3 if the bow\'s orientation is south.')
  orientation_pos_invalid = True

  if orientation == "w" and col_no < 3:
  print('The column number must be at least 3 if the bow\'s orientation is east.')
  orientation_pos_invalid = True

  if orientation == "e" and col_no > 8:
  print('The column number must not be greater than 8 if the bow\'s orientation is west.')
  orientation_pos_invalid = True

  if orientation == "n" and row_no > 8:
  print('The row number must not be greater than 8 if the bow\'s orientation is north.')
  orientation_pos_invalid = True

  if orientation_pos_invalid == True:
  wants_new_orientation = input("Would you like to choose a new orientation?")

  if wants_new_orientation.lower() == "yes":
    get_human_orientation()
  else:
  wants_new_coordinates = input("Would you like to choose new coordinates?")
  if wants_new_coordinates.lower() == "yes":
  human_places_ships()

def get_human_orientation(row_no, column_no):
  while True:
    orientation = input("How is the ship oriented? Use a single letter")
    if validate_orientation(orientation):
      break
    validate_orientation_pos(row_no, column_no, orientation)

def validate_orientations(orientation):
  possible_orientations=["n", "s", "e", "w"]

  if orientation in possible_orientations:
    return True
  else:
    print("invalid input; you must enter n, s, e or w")
    return False

def play_game():
  global bow_coordinates
  print("Welcome to Battleship (2 ships of length 3 each).")
  print(f"Board coordinates range from {BOARD_MIN} to {BOARD_MAX} on both x and y axes.")
  human_turn_choice = input("Would you like to play first?")
  
  if human_turn_choice.lower() == "yes":
    bow_coordinates.append(human_places_ships())
  else:
    bow_coordinates.append(computer_places_ships())