import turtle

# Create the drawing window
t = turtle.Turtle()

# Draw as fast as possible
t.speed(0)

# Hide the turtle arrow
t.hideturtle()

# Size of each square and number of squares per side
square_size = 40
board_size = 8

# Starting position (top-left corner of the board)
# Start at left side
x = -160

# Start at top
y = 160

# Draw 8 rows
for row in range(board_size):
  # Draw 8 columns in each row
  for col in range(board_size):
    # Move turtle to the right position
    t.penup()
    t.goto(x + col * square_size, y - row * square_size)
    t.pendown()
    
    # Figure out which color to use
    # Add row + col, if even number = red, if odd number = black
    color_value = (row + col) % 2
    
    # Draw the square with the right color
    if color_value == 0:
      t.fillcolor("red")
    else:
      t.fillcolor("black")
    
    # Fill in the square
    t.begin_fill()
    for side in range(4):
      t.forward(square_size)
      t.left(90)
    t.end_fill()

# Keep window open until you close it
turtle.done()