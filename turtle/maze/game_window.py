# turtle creates a drawing window where the game will live.
import turtle

# turtle is module that allows you to build graphical user
# interfaces or GUIs with Python.

# Create the window.

# Instantiate the Screen() class to create the game window.
window = turtle.Screen()

# Setting the text shown in the title bar of the game window.

# "Maze Game" is a positional argument.
# window.title("Maze Game")

# titlestring="Maze Game" is a keyword argument.
window.title(titlestring="Maze Game")

# The background colour of the window can be established by
# invoking the .bgcolor() method.
window.bgcolor("darkBlue")

# The size of the game window can be controlled with the help
# of the .setup() method.

# Right now, the width and height of the window is being set to
# 600 pixels.
window.setup(width=850, height=600)

# With the following approach the width and height would occupy
# fifty percent of the screen.
# window.setup(width=0.5, height=0.5)

# Create the player which will be a Turtle object.
player = turtle.Turtle()

# "arrow", "turtle", "circle", "square", "triangle", "classic"
player.shape("circle")

player.color("red")

# Allows the turtle to move across the screen without drawing a
# line.
player.penup()

# Make the square that represents the player, larger by calling
# the .shapesize() method on the Turtle object.

# .shapesize(stretch_wid=None, stretch_len=None, outline=None)

# stretch_wid is stretchfactor perpendicular to its orientation,
# stretch_len is stretchfactor in direction of its orientation,
# outline determines the width of the shape's outline.

# (stretch_wid=2, stretch_len=2) makes the square 40x40 pixels.

# (stretch_wid=1, stretch_len=1) is the default square size of
# 20x20 pixels.

# 30x30 pixels
player.shapesize(stretch_wid=0.75, stretch_len=0.75)


def move_up():
    # Before the player's vertical position changes, first the
    # player's current y-coordinate position must be found.
    y_position = player.ycor()

    # Move the player up by increasing the y-coordinate by 25.
    player.sety(y_position + 25)

def move_down():
    y_position = player.ycor()

    player.sety(y_position - 25)

def move_right():
    x_position = player.xcor()

    player.setx(x_position + 25)

def move_left():
    x_position = player.xcor()

    player.setx(x_position - 25)

# Control the positioning of the player (white square).
# The .goto() method moves the turtle.

# Passing -200 for 'x' indicates that the player will be moved
# 200 pixels to the left horizontally.

# Passing 280 pixels for 'y' means that the player will be moved
# 280 pixels vertically higher.
# player.goto(x, y)
player.goto(x=280, y=480)

# The 'X' character represents a wall in the maze.
# Each of the ten items in this maze are separated by a
# comma.
maze = [
    "X XXXXXXXXXXXXXXXXXXX XXX",
    "X     X                 X",
    "X XXX X XXXXXXXXX XXXXXXX",
    "X X   X       X   X     X",
    "X X  XXXXX XX XX      X X",
    "X XX XXX   XX XXXXX XXXXX",
    "X        X X      X  X  X",
    "XXXXXXXX XXXXX XXXX XXX X",
    "X        X              X",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Create a wall drawing with Turtle.
wall = turtle.Turtle()

wall.shape("square")
wall.color("white")

wall.shapesize(stretch_wid=1.5, stretch_len=1.5)

wall.penup()

# In turtle, the .speed() method controls how fast the turtle
# draws or moves.

# Without wall.speed(0) the turtle would slowly move to each
# position.

# speed 1 is slowest, 10 is second fastest. 0 has no animation and is fastest
wall.speed(0)

# Convert the maze text into walls.
walls = []

spacing_between_walls = 30

# Horizontally centre the maze.
# 1. Measure the maze width.

width = len(maze[0])

start_x = -350
start_y = 240

# len(maze) returns 10 because 'maze' references a list that
# contains ten items. The items are separated by commas.

# range(len(maze)) -> range(10) -> a range of 0-9.
for row in range(len(maze)):
    # 1st iteration:
    # 'row' is 0.

    # maze[0] returns "X XXXXXXXXXXXXXXXXXXX XXX" because
    # 0 is the index of the first item in 'maze'.

    # len(maze[0]) returns 25.
    for column in range(len(maze[row])):
        character = maze[row][column]

        x_coordinate = start_x + (column * spacing_between_walls)
        y_coordinate = start_y - (row * spacing_between_walls)

        if character == "X":
            wall.goto(x_coordinate, y_coordinate)

            wall.stamp()

            # Keep track of all the coordinates for each character
            # that makes up the maze.
            walls.append((x_coordinate, y_coordinate))

# Instruct the Screen object that is referenced by the variable
# named 'window' to listen for keys that are pressed on the
# user's keyboard.
window.listen()

# Bind the keys on the user's keyboard to specific functions that
# were defined in this program.

# When the Up arrow on the user's keyboard is pressed, the function
# move_up() will be invoked.
window.onkey(move_up, "Up") 
window.onkey(move_down, "Down")
window.onkey(move_left, "Left")
window.onkey(move_right, "Right")

moving_up = False
moving_left = False
moving_down = False
moving_right = False

def press_up():
    global moving_up
    moving_up = True

def press_down():
    global moving_down
    moving_down = True

def press_left():
    global moving_left
    moving_left = True

def press_right():
    global moving_right
    moving_right = True
     

def release_up():
    global moving_up
    moving_up = False

def release_down():
    global moving_down
    moving_down = False

def release_left():
    global moving_left
    moving_left = False

def release_right():
    global moving_right
    moving_right = False

window.onkeypress(press_up, "Up")
window.onkeyrelease(release_up, "Up")

window.onkeypress(press_down, "Down")
window.onkeyrelease(release_down, "Down")

window.onkeypress(press_left, "Left")
window.onkeyrelease(release_left, "Left")

window.onkeypress(press_right, "Right")
window.onkeyrelease(release_right, "Right")

def can_move(x, y):
    for wall in walls:
        if abs(x - wall[0]) < 25 and abs(y - wall[1]) < 25:
            return False
    return True

# dx represents the change in x.
# dy represents the change in y.
def move_player(dx, dy):
    new_x = player.xcor() + dx
    new_y = player.ycor() + dy

    # print("can_move(new_x, new_y):", can_move(new_x, new_y))

    if can_move(new_x, new_y):
        player.setx(new_x)
        player.sety(new_y)

def game_loop():
    if moving_up:
        move_player(0, 5)
            
    if moving_down:            
        move_player(0, -5)

    if moving_right:
        move_player(5, 0)

    if moving_left:
        move_player(-5, 0)

    # Call the function game_loop() again after twenty milliseconds.
    window.ontimer(game_loop, 20)

game_loop()

# Instruct Python that the Turtle graphics program is finished
# setting up and its window should be kept open and running.
turtle.done()