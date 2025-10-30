# Import the random module for generating random values
import random
# Import the turtle module for GUI graphics
import turtle
# Import the sys module for system operations
import sys

# Screen setup
# Create the turtle screen object
screen = turtle.Screen()
# Set the window title to "Battleship Game"
screen.title("Battleship Game")
# Set the background color to light blue
screen.bgcolor("lightblue")
# Set the window size to 600x600 pixels
screen.setup(width=600, height=600)

# Multiline comment/docstring.
'''
| Element                       | Colour  |
| ----------------------------- | ------- |
| Human ships                   | Gray    |
| Human hits on computer ships  | Red     |
| Human misses                  | White   |
| Computer hits on human ships  | Orange  |
| Computer misses (their shots) | Blue    |
'''

# Function to close the game window after a delay.
def exit_after_delay(delay=5):
    """Closes the Turtle window and exits the program after a short delay."""
    print(f"\nExiting in {delay} seconds...")

    def close_and_exit():
        # Close the turtle window.
        turtle.bye()

        print("\nGame exited successfully.")

        # Exit the program with zero indicating a success status
        # as opposed to an error status.
        sys.exit(0)

    # Schedule the closure in milliseconds; let turtle keep the UI alive
    screen.ontimer(close_and_exit, delay * 1000)

# Text display turtle
# Create a turtle object for writing messages
message_writer = turtle.Turtle()
# Hide the turtle cursor from view
message_writer.hideturtle()
# Lift the pen to prevent drawing lines
message_writer.penup()

# Position above the board
# Move the turtle to position above the board
message_writer.goto(0, 260)

# Function to display temporary messages on screen
def display_message(text, duration=2):
    """Displays a temporary message on the screen."""
    # Clear any previous messages
    message_writer.clear()

    # Write the new message in the center
    message_writer.write(text, align="center", font=("Arial", 16, "bold"))
    
    # Optional: remove message after a delay
    # Duration in milliseconds
    # Schedule message to be cleared after duration
    screen.ontimer(message_writer.clear, duration * 1000)

'''
When you use turtle.onscreenclick(), Turtle automatically
passes two arguments to your callback function:

x: the x-coordinate of the mouse click (in turtle screen
   coordinates)

y: the y-coordinate of the mouse click
'''
# Draw a quit confirmation dialog
def draw_quit_confirmation():
    """Draw a modal confirmation box with Yes/No buttons."""
    # Create a turtle for drawing the modal
    modal = turtle.Turtle()
    # Hide the turtle cursor
    modal.hideturtle()
    # Lift the pen to prevent drawing
    modal.penup()
    # Set drawing speed to instant
    modal.speed(0)

    # Modal position and size
    # Define the modal box dimensions
    box_width, box_height = 300, 150
    # Calculate the top-left corner position
    box_x, box_y = -box_width/2, box_height/2

    # Draw box background
    # Move to top-left corner of modal
    modal.goto(box_x, box_y)
    # Set fill color to light gray
    modal.fillcolor("lightgray")
    # Begin filling the rectangle
    modal.begin_fill()
    # Draw rectangle by moving forward twice
    for i in range(2):
        # Draw width of rectangle
        modal.forward(box_width)
        # Turn right 90 degrees
        modal.right(90)
        # Draw height of rectangle
        modal.forward(box_height)
        # Turn right 90 degrees
        modal.right(90)
    # Complete the filled rectangle
    modal.end_fill()

    # Draw message
    # Move to message position (centered below top)
    modal.goto(0, box_y - 50)
    # Write the quit confirmation question
    modal.write("Are you sure you want to quit?", align="center", font=("Arial", 14, "bold"))

    # Button positions
    # Define Yes button position and size (left side)
    yes_button = {'x': box_x + 40, 'y': box_y - 100, 'w': 80, 'h': 40}
    # Define No button position and size (right side)
    no_button = {'x': box_x + box_width - 120, 'y': box_y - 100, 'w': 80, 'h': 40}

    # Draw buttons
    # Loop through both Yes and No buttons
    for button, label, color in [(yes_button, "Yes", "green"), (no_button, "No", "red")]:
        # Move to button's top-left corner
        modal.goto(button['x'], button['y'])

        # Set button fill color (green or red)
        modal.fillcolor(color)

        # Begin filling the button rectangle
        modal.begin_fill()

        # Draw rectangle by looping twice
        for i in range(2):
            # Draw button width
            modal.forward(button['w'])

            # Turn right 90 degrees
            modal.right(90)

            # Draw button height
            modal.forward(button['h'])

            # Turn right 90 degrees
            modal.right(90)

        # Complete the filled button rectangle
        modal.end_fill()

        # Move to center of button for text
        modal.goto(button['x'] + button['w']/2, button['y'] - button['h']*0.75)

        # Write button label text
        modal.write(label, align="center", font=("Arial", 12, "bold"))

    # Click handler for the modal
    # Function to handle clicks on the quit confirmation modal
    def on_modal_click(x_click, y_click):
        # Check Yes button
        # Check if click is within Yes button boundaries
        if yes_button['x'] <= x_click <= yes_button['x'] + yes_button['w'] and \
           yes_button['y'] - yes_button['h'] <= y_click <= yes_button['y']:
            # Print termination message
            print("\nGame terminated by user.")

            # Closes Turtle window
            # Close the turtle graphics window
            turtle.bye()

            # The zero indicates that the Python program
            # is exiting with a success status.
            # Exit the program with success status
            sys.exit(0)

        # Check No button
        # Check if click is within No button boundaries
        if no_button['x'] <= x_click <= no_button['x'] + no_button['w'] and \
           no_button['y'] - no_button['h'] <= y_click <= no_button['y']:
            # Remove modal and restore Quit button
            # Clear the modal from screen
            modal.clear()
            # Redraw the quit button
            draw_quit_button()
            # Re-attach quit button click handler
            screen.onscreenclick(handle_quit_button)
            # Return from modal handler
            return

    # Bind the modal click handler to screen clicks
    screen.onscreenclick(on_modal_click)

# Handle clicks on the quit button
def handle_quit_button(x_click, y_click):
    """Check if the quit button is clicked and show confirmation modal."""
    # Define quit button position and size
    button_x, button_y = 200, 260
    # Set button dimensions
    width, height = 100, 40

    # Check if click is within button boundaries
    if button_x <= x_click <= button_x + width and button_y - height <= y_click <= button_y:
        # Show quit confirmation dialog
        draw_quit_confirmation()

# Draw the game title on screen
def draw_title(text="Battleship Game"):
    # Create a turtle for writing the title
    title_writer = turtle.Turtle()

    # Hide the turtle cursor
    title_writer.hideturtle()
    # Lift the pen to prevent drawing
    title_writer.penup()

    # Adjust Y coordinate for top.
    # Move to position above the board
    title_writer.goto(0, 180)

    # Write the title text centered at top
    title_writer.write(text, align="center", font=("Arial", 24, "bold"))

# Draw the legend showing color meanings
def draw_legend():
    # Create a turtle for drawing legend
    legend_writer = turtle.Turtle()
    # Hide the turtle cursor
    legend_writer.hideturtle()
    # Lift the pen to prevent drawing
    legend_writer.penup()

    # Starting position for the legend
    # Set starting position on the left side
    start_x, start_y = -500, 200
    # Move to starting position
    legend_writer.goto(start_x, start_y)
    # Write "Legend:" header
    legend_writer.write("Legend:", font=("Arial", 14, "bold"))

    # Define legend items: (label, color)
    # List of all legend entries with their colors
    legend_items = [
        ("Human ships", "gray"),
        ("Human hits on computer ships", "red"),
        ("Human misses", "white"),
        ("Computer hits on human ships", "orange"),
        ("Computer misses (their shots)", "blue"),
        ("Sunk human ship", "darkred"),
        ("Sunk computer ship", "darkgreen")
    ]

    # Size of colored square in legend
    square_size = 20

    # Vertical spacing between items
    # Spacing between legend entries
    spacing = 30

    # Draw each legend item
    # Loop through all legend items
    for i, (label, color) in enumerate(legend_items):
        # Calculate Y position for this item
        y = start_y - (i + 1) * spacing
        # Move to this item's position
        legend_writer.goto(start_x, y)
        
        # Draw colored square
        # Set the fill color for this square
        legend_writer.fillcolor(color)
        # Begin filling the square
        legend_writer.begin_fill()
        # Draw a square with 4 sides
        for i in range(4):
            # Draw one side of square
            legend_writer.forward(square_size)
            # Turn left 90 degrees
            legend_writer.left(90)
        # Complete the filled square
        legend_writer.end_fill()
        
        # Write label next to square
        # Lift pen before moving
        legend_writer.penup()
        # Move right of square
        legend_writer.forward(square_size + 10)
        # Write the label text
        legend_writer.write(label, font=("Arial", 12, "normal"))
        # Move back for next square
        legend_writer.backward(square_size + 10)

# Draw row numbers on the left side of board
def draw_row_labels():
    # Create a turtle for writing row labels
    label_writer = turtle.Turtle()
    # Hide the turtle cursor
    label_writer.hideturtle()
    # Lift the pen to prevent drawing
    label_writer.penup()
    # Size of each board square
    square_size = 30
    # Starting Y position for bottom row
    start_y = -5 * square_size

    # Track current row number
    row_number = 0

    # Draw row labels for all rows
    for i in range(BOARD_SIZE):
        # Label rows 1-10 bottom to top.
        # Increment row number from 0 to 1-10
        row_number += 1

        # Calculate Y position for this row label
        y = start_y + i * square_size + square_size/2

        # Left of grid.
        # Set X position to left of board
        x = -5 * square_size - 20
        # Move to label position
        label_writer.goto(x, y - 10)
        # Write the row number
        label_writer.write(str(row_number), font=("Arial", 12, "normal"))

# Draw column numbers below the board
def draw_column_labels():
    # Create a turtle for writing column labels
    label_writer = turtle.Turtle()
    # Hide the turtle cursor
    label_writer.hideturtle()
    # Lift the pen to prevent drawing
    label_writer.penup()
    # Size of each board square
    square_size = 30
    # Starting X position for leftmost column
    start_x = -5 * square_size

    # Draw column labels for all columns
    for i in range(BOARD_SIZE):
        # Label columns left to right.
        # Calculate column number (1-based)
        col_number = i + 1
        # Calculate X position for this column label
        x = start_x + i * square_size + square_size / 2

        # Below grid.
        # Set Y position below the board
        y = -5 * square_size - 20

        # Adjust horizontal alignment.
        # Move to label position
        label_writer.goto(x - 5, y)
        # Write the column number
        label_writer.write(str(col_number), font=("Arial", 12, "normal"))

# Draw the game board grid
def draw_board():
    # Create a turtle for drawing the board
    drawer = turtle.Turtle()
    # Hide the turtle cursor
    drawer.hideturtle()
    # Set drawing speed to instant
    drawer.speed(0)
    # Lift the pen before moving
    drawer.penup()
    
    # size of each square
    # Define size of each grid square
    square_size = 30
    # Starting X position for left edge
    start_x = -5 * square_size
    # Starting Y position for bottom edge
    start_y = -5 * square_size

    # Draw vertical lines
    # Draw each vertical line in the grid
    for i in range(BOARD_SIZE + 1):
        # Move to bottom of this vertical line
        drawer.goto(start_x + i * square_size, start_y)
        # Put pen down to start drawing
        drawer.pendown()
        # Draw line to top of board
        drawer.goto(start_x + i * square_size, start_y + BOARD_SIZE * square_size)
        # Lift pen after drawing
        drawer.penup()

    # Draw horizontal lines
    # Draw each horizontal line in the grid
    for i in range(BOARD_SIZE + 1):
        # Move to left of this horizontal line
        drawer.goto(start_x, start_y + i * square_size)
        # Put pen down to start drawing
        drawer.pendown()
        # Draw line to right of board
        drawer.goto(start_x + BOARD_SIZE * square_size, start_y + i * square_size)
        # Lift pen after drawing
        drawer.penup()

# Draw a sunk ship with special coloration
def draw_sunk_ship(ship_tiles, ship_owner="computer"):
    """
    Draw a sunk ship on the GUI.
    ship_owner: "human" or "computer"
    """
    # Create a turtle for drawing the sunk ship
    drawer = turtle.Turtle()
    # Hide the turtle cursor
    drawer.hideturtle()
    # Set drawing speed to instant
    drawer.speed(0)
    # Lift the pen before moving
    drawer.penup()
    # Size of each board square
    square_size = 30

    # Choose color based on owner
    # Determine color for sunk ship based on owner
    if ship_owner == "human":
        # human ship sunk by computer
        color = "darkred"
    elif ship_owner == "computer":
        # computer ship sunk by human
        color = "darkgreen"
    else:
        # fallback
        color = "black"

    # Draw filled squares
    # Draw filled squares for each tile of the sunk ship
    for row, col in ship_tiles:
        # Convert board coordinates to turtle coordinates
        x, y = get_turtle_position(row, col)
        # Move to bottom-left of this tile
        drawer.goto(x - square_size/2, y - square_size/2)
        # Set fill color
        drawer.fillcolor(color)
        # Begin filling the square
        drawer.begin_fill()
        # Draw a square with 4 sides
        for i in range(4):
            # Draw one side
            drawer.forward(square_size)
            # Turn left 90 degrees
            drawer.left(90)
        # Complete the filled square
        drawer.end_fill()

    # Draw black border around the sunk ship
    # Set pen color to black for border
    drawer.pencolor("black")
    # Make pen thicker for visible border
    drawer.pensize(2)

    # Draw black border around each tile
    for row, col in ship_tiles:
        # Convert board coordinates to turtle coordinates
        x, y = get_turtle_position(row, col)
        # Move to bottom-left of this tile
        drawer.goto(x - square_size/2, y - square_size/2)
        # Put pen down to start drawing border
        drawer.pendown()
        # Draw square border
        for i in range(4):
            # Draw one side
            drawer.forward(square_size)
            # Turn left 90 degrees
            drawer.left(90)
        # Lift pen after drawing
        drawer.penup()

# Draw the quit button in top-right corner
def draw_quit_button():
    """Draw a clickable 'Quit Game' button on the screen."""
    # Create a turtle for drawing the button
    button_writer = turtle.Turtle()
    # Hide the turtle cursor
    button_writer.hideturtle()
    # Lift the pen before moving
    button_writer.penup()
    
    # Position of the button
    # Set button position in top-right area
    button_x, button_y = 200, 260
    # Set button dimensions
    width, height = 100, 40

    # Draw rectangle for button
    # Move to top-left corner of button
    button_writer.goto(button_x, button_y)
    # Put pen down to start drawing
    button_writer.pendown()
    # Set button fill color to red
    button_writer.fillcolor("red")
    # Begin filling the rectangle
    button_writer.begin_fill()

    # Draw rectangle by looping twice
    for i in range(2):
        # Draw button width
        button_writer.forward(width)
        # Turn right 90 degrees
        button_writer.right(90)
        # Draw button height
        button_writer.forward(height)
        # Turn right 90 degrees
        button_writer.right(90)
    # Complete the filled rectangle
    button_writer.end_fill()
    # Lift pen after drawing
    button_writer.penup()
    
    # Write text on button
    # Move to center of button for text
    button_writer.goto(button_x + width/2, button_y - height*0.75)
    # Write "Quit Game" text
    button_writer.write("Quit Game", align="center", font=("Arial", 12, "bold"))

    # Define click handler
    # Function to handle clicks on quit button
    def on_click(x_click, y_click):
        # Check if click is within button boundaries
        if button_x <= x_click <= button_x + width and button_y - height <= y_click <= button_y:
            # Show the quit confirmation modal.
            # Show quit confirmation dialog
            draw_quit_confirmation()

    # Bind the click to the screen
    # Attach click handler to screen
    screen.onscreenclick(on_click)

# Check if a ship is completely sunk
def ship_is_sunk(ship, hits):
    """Return True if all tiles of a ship are in the hit list."""
    # Return True if all ship tiles are in hits set
    return all(tile in hits for tile in ship)

# Convert board coordinates to turtle screen coordinates
def get_turtle_position(row, col):
    """Convert board coordinates (1-10) to turtle coordinates."""
    # Size of each board square
    square_size = 30

    # col 1 maps to -150
    # Convert column to X coordinate
    x = (col - 6) * square_size + square_size/2

    # row 1 maps to -150
    # Convert row to Y coordinate
    y = (row - 6) * square_size + square_size/2
    # Return the turtle coordinates
    return x, y

# Global turtle object for drawing ships and shots
drawer = turtle.Turtle()
# Hide the turtle cursor
drawer.hideturtle()
# Set drawing speed to instant
drawer.speed(0)
# Lift the pen before moving
drawer.penup()

# Draw a ship on the board
def draw_ship(tiles, color="gray"):
    # Size of each board square
    square_size = 30

    # Draw each tile of the ship
    for row, col in tiles:
        # Convert board coords to turtle coords
        x, y = get_turtle_position(row, col)
        # Move to bottom-left of tile
        drawer.goto(x - square_size/2, y - square_size/2)
        # Set fill color
        drawer.fillcolor(color)
        # Begin filling the square
        drawer.begin_fill()

        # Draw square with 4 sides
        for i in range(4):
            # Draw one side
            drawer.forward(square_size)
            # Turn left 90 degrees
            drawer.left(90)

        # Complete the filled square
        drawer.end_fill()

# Draw a hit marker on the board
def draw_hit(row, col, color="red"):
    # Convert board coords to turtle coords
    x, y = get_turtle_position(row, col)
    # Move to center of tile
    drawer.goto(x, y - 10)
    # Set dot color
    drawer.color(color)
    # Draw a dot to mark hit
    drawer.dot(20)

# Draw a miss marker on the board
def draw_miss(row, col, color="white"):
    # Convert board coords to turtle coords
    x, y = get_turtle_position(row, col)
    # Move to center of tile
    drawer.goto(x, y - 10)
    # Set dot color
    drawer.color(color)
    # Draw a dot to mark miss
    drawer.dot(20)

# Draw axis titles for rows and columns
def draw_axis_titles():
    # Create a turtle for writing axis titles
    label_writer = turtle.Turtle()
    # Hide the turtle cursor
    label_writer.hideturtle()
    # Lift the pen before moving
    label_writer.penup()
    # Size of each board square
    square_size = 30

    # Column axis title
    # Center X position for "Columns" label
    x_center = 0

    # A bit below column numbers.
    # Calculate Y position below column labels
    y_below_grid = -5 * square_size - 50
    # Move to columns label position
    label_writer.goto(x_center, y_below_grid)
    # Write "Columns" label
    label_writer.write("Columns", align="center", font=("Arial", 14, "bold"))

    # Row axis title
    # A bit left of row numbers.
    # Calculate X position left of row labels
    x_left_of_grid = -5 * square_size - 70
    # Center Y position for "Rows" label
    y_center = 0
    # Move to rows label position
    label_writer.goto(x_left_of_grid, y_center)
    # Write "Rows" label
    label_writer.write("Rows", align="center", font=("Arial", 14, "bold"))

# Random row for computer's first shot (unused variable)
computer_row = random.randint(1, 10)
# Random column for computer's first shot (unused)
computer_column = random.randint(1, 10)

# Game configuration constants
# Length of each ship in tiles
SHIP_LENGTH = 3
# Number of ships each player has
NUM_OF_SHIPS = 2
# Minimum board coordinate (1-based)
BOARD_MIN = 1
# Maximum board coordinate (1-based)
BOARD_MAX = 10
# Board size (10x10 grid)
BOARD_SIZE = 10
# Possible ship orientations
ORIENTATIONS = ['n', 's', 'e', 'w']

# Validate that input is a number between 1 and 10
def coordinate_is_valid(column_or_row):
    # Try to convert input to integer
    try:
        int(column_or_row)
    # Catch value error if conversion fails
    except ValueError:
        # Print error message for non-numeric input
        print("Error: You must input a number from 1 to 10!")
        # Return False for invalid input
        return False

    # Check if value is in valid range
    if 1 <= column_or_row <= 10:
        # Return True for valid coordinate
        return True
    else:
        # Return False for out-of-range coordinate
        return False

# Check if coordinates are within board boundaries
def in_bounds(row, col):
    """Check if a coordinate is within 1..10"""
    # Print coordinates for debugging
    # print(f'row: {row}, col: {col}')

    # Print bounds check result for debugging
    # print(1 <= row <= BOARD_SIZE and 1 <= col <= BOARD_SIZE)

    # Return True if both coordinates are in bounds
    return 1 <= row <= BOARD_SIZE and 1 <= col <= BOARD_SIZE

# Check if all ship tiles fit within the board
def ship_fits(tiles):
    """Check if all ship tiles are inside the board"""
    # Check each tile of the ship
    for r, c in tiles:
        # If any tile is out of bounds
        if not in_bounds(r, c):
            # Print failure message
            print('The ship didn\'t fit.')
            # Return False if ship doesn't fit
            return False
    # Print success message
    print('The ship fits.')
    # Return True if ship fits
    return True

# Check if ship tiles are not already occupied
def tiles_free(tiles, occupied):
    """Check if all ship tiles are free (not overlapping)"""
    # Check each tile of the ship
    for r, c in tiles:
        # If tile is already in occupied set
        if (r, c) in occupied:
            # Print failure message
            print('The tiles weren\'t free.')
            # Return False if tiles overlap
            return False
    # Print success message
    print('The tiles are free.')
    # Return True if all tiles are free
    return True

# Generate list of tile coordinates for a ship
def gen_ship_tiles(bow_row, bow_col, orientation):
    """Return a list of 3 coordinates for the ship"""
    # Check if ship faces north
    if orientation == 'n':
        # Generate tiles going north (decreasing row)
        return [(bow_row - i, bow_col) for i in range(SHIP_LENGTH)]
    # Check if ship faces south
    elif orientation == 's':
        # Generate tiles going south (increasing row)
        return [(bow_row + i, bow_col) for i in range(SHIP_LENGTH)]
    # Check if ship faces east
    elif orientation == 'e':
        # Generate tiles going east (decreasing col)
        return [(bow_row, bow_col - i) for i in range(SHIP_LENGTH)]
    # Check if ship faces west
    elif orientation == 'w':
        # Generate tiles going west (increasing col)
        return [(bow_row, bow_col + i) for i in range(SHIP_LENGTH)]

# Set to track all occupied board tiles
occupied_tiles = set()

# Computer places a single ship randomly
def computer_places_ships():
    """Randomly choose a valid bow and orientation for a ship"""
    # Keep trying until valid placement found
    while True:
        # Pick random row for ship bow
        bow_row = random.randint(1, BOARD_SIZE)
        # Pick random column for ship bow
        bow_col = random.randint(1, BOARD_SIZE)
        # Pick random orientation
        orientation = random.choice(ORIENTATIONS)

        # Generate tile coordinates for this ship
        tiles = gen_ship_tiles(bow_row, bow_col, orientation)

        # Check if ship is within bounds and doesn't overlap
        # If ship placement is valid
        if ship_fits(tiles) and tiles_free(tiles, occupied_tiles):
            # Print success message
            print("The computer placed its ships.")
            # Return the ship tiles
            return tiles

# Check if ship orientation and position are compatible
def validate_orientation_pos(row_no, col_no, orientation):
    # Track if validation fails
    orientation_pos_invalid = False

    # Print current values for debugging
    print(f'\nrow_no: {row_no}\ncol_no: {col_no}')

    # Print blank line for readability
    print()

    # Check north orientation: row must be at least 3
    if orientation == "n" and row_no < 3:
        # Print error for north orientation
        print("The row number must not be less than 3 if the bow's orientation is north.")
        # Mark validation as failed
        orientation_pos_invalid = True

    # Check south orientation: row must be at most 8
    if orientation == "s" and row_no > 8:
        # Print error for south orientation
        print("The row number must not be greater than 8 if the bow's orientation is south.")
        # Mark validation as failed
        orientation_pos_invalid = True

    # Check east orientation: column must be at least 3
    if orientation == "e" and col_no < 3:
        # Print error for east orientation
        print("The column number must not be less than 3 if the bow's orientation is east.")
        # Mark validation as failed
        orientation_pos_invalid = True

    # Check west orientation: column must be at most 8
    if orientation == "w" and col_no > 8:
        # Print error for west orientation
        print("The column number must be less than 9 if the bow's orientation is west.")
        # Mark validation as failed
        orientation_pos_invalid = True

    # If any validation failed
    if orientation_pos_invalid:
        # Print invalid message
        print('The orientation is invalid.')
        # Return False for invalid
        return False
    else:
        # Print valid message
        print('The orientation is valid.')
        # Return True for valid
        return True

# Validate that orientation letter is valid
def validate_orientations(orientation):
    # Check if orientation is in valid list
    if orientation in ORIENTATIONS:
        # Return True for valid orientation
        return True
    else:
        # Print error for invalid orientation
        print("Invalid input; you must enter n, s, e or w.")
        # Return False for invalid
        return False

# Duplicate function (same as earlier definition)
# Validate that input is a number between 1 and 10
def coordinate_is_valid(column_or_row):
    # Try to convert input to integer
    try:
        # Store converted value
        value = int(column_or_row)
    # Catch value error if conversion fails
    except ValueError:
        # Print error message for non-numeric input
        print("Error: You must input a number from 1 to 10!")
        # Return False for invalid input
        return False
    # Check if value is in valid range
    if 1 <= value <= 10:
        # Return True for valid coordinate
        return True
    else:
        # Print error for out-of-range value
        print("Out of range! Choose from 1 to 10.")
        # Return False for out-of-range
        return False

# Get ship orientation from human player
def get_human_orientation(row_no, col_no):
    """
    Prompt the human player for orientation, ensuring the ship fits.
    If the ship does not fit, ask if they want to change orientation or coordinates.
    """
    # Keep asking until valid orientation
    while True:
        # Prompt user for orientation letter
        orientation = input("\nHow is the ship oriented? Use a single letter (n/s/e/w): ").lower()
        # If orientation letter is invalid
        if not validate_orientations(orientation):
            # invalid letter, ask again
            continue

        # If orientation position is valid
        if validate_orientation_pos(row_no, col_no, orientation):
            # valid orientation that fits
            return orientation

        # Ship does not fit, ask player what to do
        # Print message about ship not fitting
        print("\nThe chosen orientation causes the ship not to fit.")
        # Ask if user wants different orientation
        change_orientation = input('Enter "yes" if you would like to choose a different orientation: ').lower()
        # If user wants different orientation
        if change_orientation == "yes":
            # loop back to ask orientation again
            continue

        # Ask if user wants different coordinates
        change_coordinates = input('Enter "yes" if you would like to choose different coordinates: ').lower()
        # If user wants different coordinates
        if change_coordinates == "yes":
            # signal to choose new coordinates
            return None
        else:
            # Print message to try again
            print("You must choose a valid orientation or coordinates. Try again.")

# Human player places one ship
def human_places_ships():
    """
    Prompt human player to place a single ship. Ensures ship is valid and does not overlap.
    Repeats until a valid ship is placed.
    """
    # Keep trying until valid ship placed
    while True:
        # Get bow coordinates
        # Loop to get valid column
        while True:
            # Prompt for column input
            col_input = input("From 1 to 10, choose a column for the ship's bow: ")
            # If column input is valid
            if coordinate_is_valid(col_input):
                # Convert to integer
                col_no = int(col_input)
                # Break out of column loop
                break

        # Loop to get valid row
        while True:
            # Prompt for row input
            row_input = input("From 1 to 10, choose a row for the ship's bow: ")
            # If row input is valid
            if coordinate_is_valid(row_input):
                # Convert to integer
                row_no = int(row_input)
                # Break out of row loop
                break

        # Get orientation
        # Get orientation from user
        orientation = get_human_orientation(row_no, col_no)
        # If user chose to change coordinates
        if orientation is None:
            # Player chose new coordinates
            continue

        # Generate ship tiles
        tiles = gen_ship_tiles(row_no, col_no, orientation)

        # Check if ship fits and doesn't overlap
        if ship_fits(tiles) and tiles_free(tiles, occupied_tiles):
            # Add ship tiles to occupied set
            occupied_tiles.update(tiles)
            # Print success message
            print("Ship placed successfully!")
            # Return ship tiles
            return tiles
        else:
            # Print error message
            print("Invalid position or overlap. Try again.\n")

# Computer places all its ships
def computer_places_all_ships():
    # List to hold computer ships
    computer_ships = []

    # Place each ship
    for i in range(NUM_OF_SHIPS):
        # Place one ship
        tiles = computer_places_ships()
        # Add ship tiles to occupied set
        occupied_tiles.update(tiles)
        # Add ship to ship list
        computer_ships.append(tiles)
    # Return all computer ships
    return computer_ships

# Human places all their ships
def human_places_all_ships():
    # List to hold human ships
    human_ships = []
    # Place each ship
    for i in range(NUM_OF_SHIPS):
        # Print ship number prompt
        print(f"\nPlace ship #{i + 1}:")
        # Place one ship
        tiles = human_places_ships()
        # Add ship to ship list
        human_ships.append(tiles)
    # Return all human ships
    return human_ships

# Check if all ships are sunk
def all_sunk(ships, hits):
    """Check if all ship tiles are in the hit list."""
    # Return True if all ship tiles are in hits
    return all(tile in hits for ship in ships for tile in ship)

# Main game loop - play alternating turns
def play_round(human_ships, computer_ships):
    # Sets to track human hits and misses
    human_hits, human_misses = set(), set()
    # Sets to track computer hits and misses
    computer_hits, computer_misses = set(), set()

    # Set to track sunk computer ships
    sunk_computer_ships = set()
    # Set to track sunk human ships
    sunk_human_ships = set()

    # Start with human turn
    turn = "human"

    # Game loop continues until someone wins
    while True:
        # Check if it's human's turn
        if turn == "human":
            # Print turn message
            print("\nYour turn to fire!")
            # Get firing coordinates from user
            try:
                # Get row from user
                row = int(input("Row (1-10): "))
                # Get column from user
                col = int(input("Column (1-10): "))
            # Handle non-numeric input
            except ValueError:
                # Print error message
                print("Invalid input.")
                # Skip to next iteration
                continue

            # Check if coordinates are in bounds
            if not in_bounds(row, col):
                # Print error message
                print("Out of bounds!")
                # Skip to next iteration
                continue

            # Check if hit
            # Variable to hold hit ship
            hit_ship = None
            # Loop through computer ships
            for ship in computer_ships:
                # Check if shot hit this ship
                if (row, col) in ship:
                    # Mark this ship as hit
                    hit_ship = ship
                    # Exit loop
                    break

            # Check if shot was a hit
            if hit_ship:
                # Print hit message
                print("💥 Human player hit a computer ship!")
                # Add hit to hit set
                human_hits.add((row, col))
                # Draw hit marker on screen
                draw_hit(row, col, color="red")

                # Check if this ship is now sunk
                # Check if ship is sunk and not already marked
                if ship_is_sunk(hit_ship, human_hits) and tuple(hit_ship) not in sunk_computer_ships:
                    # Print sunk message
                    print("🔥 You sank a computer ship!")

                    # Draw sunk ship on screen
                    draw_sunk_ship(hit_ship, ship_owner="computer")

                    # Mark ship as sunk
                    sunk_computer_ships.add(tuple(hit_ship))

                    # Display message on screen
                    display_message("🔥 You sank a computer ship!")

            # If shot was a miss
            else:
                # Print miss message
                print("💧 Human player missed.")
                # Add miss to miss set
                human_misses.add((row, col))
                # Draw miss marker on screen
                draw_miss(row, col, color="white")

            # Check for victory
            # Check if all computer ships are sunk
            if all_sunk(computer_ships, human_hits):
                # Display victory message
                display_message("🎉 You sank all computer ships!", duration=10000)

                # Print victory message
                print("🎉 You sank all computer ships! You have won the game!")

                # Exit game after delay
                exit_after_delay(10)

                # Exit game loop
                break

            # Switch to computer turn
            turn = "computer"

        # Computer's turn
        else:
            # Computer turn
            # Print computer turn message
            print("\nComputer's turn...")
            # Keep trying until unique shot found
            while True:
                # Pick random row
                row = random.randint(1, 10)
                # Pick random column
                col = random.randint(1, 10)

                # Check if shot hasn't been tried
                if (row, col) not in computer_hits and (row, col) not in computer_misses:
                    # Exit loop
                    break
            # Print computer's shot coordinates
            print(f"Computer fires at ({row}, {col})")

            # Variable to hold hit ship
            hit_ship = None
            # Loop through human ships
            for ship in human_ships:
                # Check if shot hit this ship
                if (row, col) in ship:
                    # Mark this ship as hit
                    hit_ship = ship
                    # Exit loop
                    break

            # Check if shot was a hit
            if hit_ship:
                # Print hit message
                print("💥 Computer hit your ship!")
                # Add hit to hit set
                computer_hits.add((row, col))
                # Draw hit marker on screen
                draw_hit(row, col, color="orange")

                # Check if ship is sunk and not already marked
                if ship_is_sunk(hit_ship, computer_hits) and tuple(hit_ship) not in sunk_human_ships:
                    # Print sunk message
                    print("🔥 The computer sank one of your ships!")

                    # Draw sunk ship on screen
                    draw_sunk_ship(hit_ship, ship_owner="human")

                    # Mark ship as sunk
                    sunk_human_ships.add(tuple(hit_ship))

                    # Display message on screen
                    display_message("🔥 Your ship was sunk!")

            # If shot was a miss
            else:
                # Print miss message
                print("💧 Computer missed.")
                # Add miss to miss set
                computer_misses.add((row, col))
                # Draw miss marker on screen
                draw_miss(row, col, color="blue")

            # Check if all human ships are sunk
            if all_sunk(human_ships, computer_hits):
                # Display loss message
                display_message("😢 The computer sank all your ships!", duration=5000)

                # Print loss message
                print("😢 The computer sank all your ships! The computer has won the game.")

                # Exit game after delay
                exit_after_delay(10)

                # Exit game loop
                break

            # Switch to human turn
            turn = "human"

        # Update the screen each turn
        # Refresh the turtle screen display
        turtle.getscreen().update()

# Main game initialization and setup
def play_game():
    # Disable animation for faster drawing.
    # Turn off turtle animation for instant drawing
    screen.tracer(0)

    # Draw the game board grid
    draw_board()

    # Draw the game title
    draw_title("Battleship Game")

    # Draw the color legend
    draw_legend()

    # Draw row number labels
    draw_row_labels()

    # Draw column number labels
    draw_column_labels()

    # Draw axis titles
    draw_axis_titles()

    # Draw the quit button
    draw_quit_button()

    # Update screen to show all drawings
    screen.update()

    # Print welcome message
    print("Welcome to Battleship (2 ships of length 3 each).")
    # Print board coordinate information
    print(f"Board coordinates range from {BOARD_MIN} to {BOARD_MAX} on both x and y axes.")

    # human_turn_choice = input("\nEnter \"yes\" if you would like to play first: ")
    # Auto-set human to go first (turn input disabled)
    human_turn_choice = "yes"

    # Check if human goes first
    if human_turn_choice.lower() == "yes":
        # Place ships
        # Print section header
        print("\n=== Human Player Ship Placement ===")
        # Get all human ships
        human_ships = human_places_all_ships()

        # Flatten ships into list of all tiles
        human_tiles = [tile for ship in human_ships for tile in ship]

        # Print human tiles for debugging
        print('human_tiles:', human_tiles)

        # Draw human ships on screen
        draw_ship(human_tiles, color="gray")

        # Update screen to show ships
        screen.update()

        # Print section header
        print("\n=== Computer Player Ship Placement ===")
        # Get all computer ships
        computer_ships = computer_places_all_ships()
    # If human doesn't go first
    else:
        # Place ships
        # Print section header
        print("\n=== Computer Player Ship Placement ===")

        # Get all computer ships
        computer_ships = computer_places_all_ships()

        # Print section header
        print("\n=== Human Player Ship Placement ===")

        # Get all human ships
        human_ships = human_places_all_ships()

    # Print human ships for debugging
    print("\nHuman player ships:", human_ships)

    print("\nComputer player ships:", computer_ships)

    # Play game
    # Start the main game loop
    play_round(human_ships, computer_ships)

# Start the game
play_game()

turtle.mainloop()