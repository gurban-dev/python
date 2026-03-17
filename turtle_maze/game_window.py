# turtle creates a drawing window where the game will live.
import turtle

# Create the window.

# The Screen() function creates the game window.
window = turtle.Screen()

# Setting the text shown in the title bar of the game window.

# "Maze Game" is a positional argument.
# window.title("Maze Game")

# titlestring="Maze Game" is a keyword argument.
window.title(titlestring="Maze Game")

# The background colour of the window can be established by
# invoking the .bgcolor() method.
window.bgcolor("aqua")

# The size of the game window can be controlled with the help
# of the .setup() method.

# Right now, the width and height of the window is being set to
# 600 pixels.
window.setup(width=600, height=600)

# With the following approach the width and height would occupy
# fifty percent of the screen.
# window.setup(width=0.5, height=0.5)

# Instruct Python that the Turtle graphics program is finished
# setting up and its window should be kept open and running.
turtle.done()

# Create player
player = turtle.Turtle()
player.shape("square")
player.color("white")
player.penup()