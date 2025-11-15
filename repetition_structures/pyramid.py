import turtle

'''
Write a program that draws a pyramid of circles based
on user input.

Ask the user how many circles they want on the bottom
of the pyramid and then draw a pyramid of circles,
subtracting one circle from each row.

Follow these guidelines:
1. Create a variable called row_value to keep track of
   rows of circles.
2. Use a variable called radius to set the radius value
   to 25 at the start of your code. This will make it
   easier to manipulate in the future.
'''

# Set up the screen.
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Pyramid of Circles")

# Create turtle.
t = turtle.Turtle()
t.speed(0)
t.penup()

# Circle properties.
radius = 25
spacing = 50

# Number of rows in pyramid.
no_of_rows = 6

# Draw the pyramid.
for row in range(no_of_rows):
  # Calculate number of circles in this row.
  no_of_circles = row + 1

  # Calculate starting x position to center the row.
  start_x = -(no_of_circles - 1) * spacing / 2

  # Calculate y position (higher rows go up).
  y = -row * spacing

  # Draw circles in this row.
  for circle in range(no_of_circles):
    x = start_x + circle * spacing
    t.goto(x, y)
    t.pendown()
    t.circle(radius)
    t.penup()

# Draw a black marker on top of the first row's circle.
marker_x = 0

# Top of the circle (radius goes down from pen position).
# Begin from -25 to adjust the vertical position.
marker_y = -25 + (2 * radius)

t.goto(marker_x, marker_y)

# Draw a black dot with size 10.
t.dot(20, "black")

# Hide turtle and keep window open.
t.hideturtle()
turtle.done()