import turtle

# Create the drawing window and turtle
t = turtle.Turtle()

# Make the turtle draw as quickly as possible
t.speed(0)

# Hide the turtle arrow so we only see the drawing
t.hideturtle()

# Define the dimensions of our checkerboard

# Each square will be 40 pixels wide.
square_size = 40

# We'll draw an 10x10 grid of squares.
board_size = 10

# Set the starting position for the top-left corner of the board.

# Horizontal position: left side of the screen.
horizontal_pos = -200

# Vertical position: top of the screen.
vertical_pos = 160

# Loop through each row of the checkerboard.
for row in range(board_size):
  # Loop through each column in the current row.
  for col in range(board_size):
    # Position the turtle at the correct location for this square.

    # Lift the pen so we don't draw while moving.
    t.penup()

    t.goto(horizontal_pos + col * square_size, vertical_pos - row * square_size)

    # Put the pen down to start drawing.
    t.pendown()

    # Calculate which color this square should be
    # By adding row + col, we get an alternating pattern
    # Even sums (0, 2, 4...) will be red, odd sums (1, 3, 5...) will be black
    color_value = (row + col) % 2
    
    # Set the fill color based on whether color_value is even or odd.
    if color_value == 0:
      # Set both pen and fill color to red.
      t.color("black")

      # Start filling with the current color.
      t.begin_fill()
    else:
      # Set both pen and fill color to black.
      t.color("red")

      # Start filling with the current color.
      t.begin_fill()
    
    # Draw all 4 sides of the square.
    for side in range(4):
      t.forward(square_size)

      t.left(90)

    # Finish filling the shape.
    t.end_fill()

# Keep the window open until the user closes it.
turtle.done()