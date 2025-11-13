import turtle

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
  num_circles = row + 1
  
  # Calculate starting x position to center the row.
  start_x = -(num_circles - 1) * spacing / 2
  
  # Calculate y position (higher rows go up).
  y = -row * spacing

  # Draw circles in this row.
  for circle in range(num_circles):
    x = start_x + circle * spacing
    t.goto(x, y)
    t.pendown()
    t.circle(radius)
    t.penup()

# Hide turtle and keep window open.
t.hideturtle()
turtle.done()