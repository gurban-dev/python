# Question:
# If the turtle module is going to be used in this program, what
# is the first line of code that must be written?

# Answer:
# Import the turtle module.
import turtle

# A Screen object represents the drawing window or canvas where
# the turtle graphics will appear.

# Question:
# How can the screen be created for a turtle program?

# Answer:
# Use the Screen() class that exists inside of the turtle module.
screen = turtle.Screen()

# Question:
# How can the title be set for a screen in a turtle program?

# Answer:
# Use the .title() method to set the title for a screen in a turtle program.
screen.title("Turtle Square")

# Question:
# How can the window for the turtle program be kept open?

# Answer:
# Invoke the .mainloop() method on the Screen object.
screen.mainloop()