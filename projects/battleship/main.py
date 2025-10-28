import random
import pdb

computer_row = random.randint(1, 10)
computer_column = random.randint(1, 10)

SHIP_LENGTH = 3
NUM_OF_SHIPS = 2
BOARD_MIN = 1
BOARD_MAX = 10
BOARD_SIZE = 10
ORIENTATIONS = ['n', 's', 'e', 'w']

def coordinate_is_valid(column_or_row):
    try:
        int(column_or_row)
    except ValueError:
        print("Error: You must input a number from 1 to 10!")
        return False

    if 1 <= column_or_row <= 10:
        return True
    else:
        return False

def in_bounds(row, col):
    """Check if a coordinate is within 1..10"""
    print(f'row: {row}, col: {col}')
    print(1 <= row <= BOARD_SIZE and 1 <= col <= BOARD_SIZE)

    return 1 <= row <= BOARD_SIZE and 1 <= col <= BOARD_SIZE

def ship_fits(tiles):
    """Check if all ship tiles are inside the board"""
    for r, c in tiles:
        if not in_bounds(r, c):
            print('The ship didn\'t fit.')
            return False
    print('The ship fits.')
    return True

def tiles_free(tiles, occupied):
    """Check if all ship tiles are free (not overlapping)"""
    for r, c in tiles:
        if (r, c) in occupied:
            print('The tiles weren\'t free.')
            return False
    print('The tiles are free.')
    return True

occupied_tiles = set()

def computer_places_ships():
    """Randomly choose a valid bow and orientation for a ship"""
    while True:
        bow_row = random.randint(1, BOARD_SIZE)
        bow_col = random.randint(1, BOARD_SIZE)
        orientation = random.choice(ORIENTATIONS)

        tiles = gen_ship_tiles(bow_row, bow_col, orientation)

        # Check if ship is within bounds and doesn't overlap
        if ship_fits(tiles) and tiles_free(tiles, occupied_tiles):
            print("The computer placed its ships.")
            return tiles


def gen_ship_tiles(bow_row, bow_col, orientation):
    """Return a list of 3 coordinates for the ship"""
    if orientation == 'n':
        return [(bow_row + i, bow_col) for i in range(SHIP_LENGTH)]
    elif orientation == 's':
        return [(bow_row - i, bow_col) for i in range(SHIP_LENGTH)]
    elif orientation == 'e':
        return [(bow_row, bow_col - i) for i in range(SHIP_LENGTH)]
    elif orientation == 'w':
        return [(bow_row, bow_col + i) for i in range(SHIP_LENGTH)]


def human_places_ships():
    while True:
        column_no = input("From 1 to 10, choose a column to place the ship's bow: ")

        if coordinate_is_valid(column_no):
            column_no = int(column_no)
            break

    while True:
        row_no = input("From 1 to 10, choose a row to place the ship's bow: ")

        if coordinate_is_valid(row_no):
            row_no = int(row_no)
            break

    orientation = get_human_orientation(row_no, column_no)

    print('orientation:', orientation)

    tiles = gen_ship_tiles(row_no, column_no, orientation)

    print('tiles:', tiles)

    if ship_fits(tiles) and tiles_free(tiles, occupied_tiles):
        occupied_tiles.update(tiles)

        print("Ship placed successfully!")

        return tiles
    else:
        print("Invalid position or overlap. Try again.\n")

        return human_places_ships()

def validate_orientation_pos(row_no, col_no, orientation):
    orientation_pos_invalid = False

    print()

    if orientation == "n" and row_no > 8:
        print("The row number must not be greater than 8 if the bow's orientation is north.")
        orientation_pos_invalid = True

    if orientation == "s" and row_no < 3:
        print("The row number must not be less than 3 if the bow's orientation is south.")
        orientation_pos_invalid = True

    if orientation == "e" and col_no < 3:
        print("The column number must not be less than 3 if the bow's orientation is east.")
        orientation_pos_invalid = True

    if orientation == "w" and col_no < 9:
        print("The column number must be less than 9 if the bow's orientation is west.")
        orientation_pos_invalid = True

    if orientation_pos_invalid:
        # Add an empty line in the output.
        print()

        wants_new_orientation = input("Enter \"yes\" if you would like to choose a new orientation: ")

        if wants_new_orientation.lower() == "yes":
            return False
        else:
            wants_new_coordinates = input("Enter \"yes\" if you would like to choose new coordinates: ")

            if wants_new_coordinates.lower() == "yes":
                human_places_ships()
    else:
        print('The orientation is valid.')
        return True

def validate_orientations(orientation):
    if orientation in ORIENTATIONS:
        return True
    else:
        print("Invalid input; you must enter n, s, e or w.")
        return False

def coordinate_is_valid(column_or_row):
    try:
        value = int(column_or_row)
    except ValueError:
        print("Error: You must input a number from 1 to 10!")
        return False
    if 1 <= value <= 10:
        return True
    else:
        print("Out of range! Choose from 1 to 10.")
        return False

def get_human_orientation(row_no, column_no):
    while True:
        orientation = input("\nHow is the ship oriented? Use a single letter (n/s/e/w): ").lower()

        valid_choice = validate_orientations(orientation)

        choice_compatible = validate_orientation_pos(row_no, column_no, orientation)

        print('\nvalid_choice:', valid_choice)
        print('choice_compatible:', choice_compatible)

        if valid_choice and choice_compatible:
            print('182 orientation:', orientation)
            return orientation

def computer_places_all_ships():
    computer_ships = []
    for _ in range(NUM_OF_SHIPS):
        tiles = computer_places_ships()
        occupied_tiles.update(tiles)
        computer_ships.append(tiles)
    return computer_ships

def human_places_all_ships():
    human_ships = []
    for i in range(NUM_OF_SHIPS):
        print(f"\nPlace ship #{i + 1}:")
        tiles = human_places_ships()
        human_ships.append(tiles)
    return human_ships

def all_sunk(ships, hits):
    """Check if all ship tiles are in the hit list."""
    return all(tile in hits for ship in ships for tile in ship)

def play_round(human_ships, computer_ships):
    human_hits, human_misses = set(), set()
    computer_hits, computer_misses = set(), set()

    turn = "human"
    while True:
        if turn == "human":
            print("\nYour turn to fire!")
            try:
                row = int(input("Row (1-10): "))
                col = int(input("Column (1-10): "))
            except ValueError:
                print("Invalid input.")
                continue

            if not in_bounds(row, col):
                print("Out of bounds!")
                continue

            if any((row, col) in ship for ship in computer_ships):
                print("💥 Hit!")
                human_hits.add((row, col))
            else:
                print("💧 Miss.")
                human_misses.add((row, col))

            if all_sunk(computer_ships, human_hits):
                print("🎉 You sank all the computer’s ships!")
                break
            turn = "computer"

        else:
            print("\nComputer's turn...")
            row = random.randint(1, 10)
            col = random.randint(1, 10)
            print(f"Computer fires at ({row}, {col})")

            if any((row, col) in ship for ship in human_ships):
                print("💥 Computer hit your ship!")
                computer_hits.add((row, col))
            else:
                print("💧 Computer missed.")
                computer_misses.add((row, col))

            if all_sunk(human_ships, computer_hits):
                print("😢 The computer sank all your ships!")
                break
            turn = "human"

def play_game():
    print("Welcome to Battleship (2 ships of length 3 each).")
    print(f"Board coordinates range from {BOARD_MIN} to {BOARD_MAX} on both x and y axes.")

    # human_turn_choice = input("\nEnter \"yes\" if you would like to play first: ")
    human_turn_choice = "yes"

    if human_turn_choice.lower() == "yes":
        # Place ships
        print("\n=== Human Player Ship Placement ===")
        human_ships = human_places_all_ships()

        print("\n=== Computer Player Ship Placement ===")
        computer_ships = computer_places_all_ships()
    else:
        # Place ships
        print("\n=== Computer Player Ship Placement ===")
        computer_ships = computer_places_all_ships()

        print("\n=== Human Player Ship Placement ===")
        human_ships = human_places_all_ships()

    print("\nHuman player ships:", human_ships)

    print("\nComputer player ships:", computer_ships)

    # Play game
    play_round(human_ships, computer_ships)

play_game()