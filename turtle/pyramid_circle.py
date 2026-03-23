import turtle

'''
Write a program that draws a pyramid of circles based on user input.

Ask the user how many circles they want on the bottom of the pyramid
and then draw a pyramid of circles, subtracting one circle from each
row.

Follow these guidelines:
1. Create a variable called row_value to keep track of rows of circles.

2. Use a variable called radius to set the radius value to 25 at the
   start of your code. This will make it easier to manipulate in the
   future.
'''

t = turtle.Turtle()

t.speed(0)
t.penup()
row_value = 0
radius = 25

def move_to_row(no_of_circles):
	x_value = -((no_of_circles - 1) * 50) / 2
	y_value = -200 + (50 * row_value)

	t.setposition(x_value, y_value)

def draw_block_row(no_of_circles):
	for _ in range(no_of_circles):
		t.pendown()
		t.circle(radius)
		t.penup()
		t.forward(50)

no_of_circles = int(input('How many circles should be on the bottom row? '))

for _ in range(no_of_circles):
	move_to_row(no_of_circles)
	draw_block_row(no_of_circles)

	row_value += 1
	no_of_circles -= 1

# Hide turtle and keep window open.
t.hideturtle()

turtle.done()