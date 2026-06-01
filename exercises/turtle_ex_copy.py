# ============================================================
# EXERCISE: REACH THE GOAL
# ============================================================
#
# Your Mission:
#
# Move the red player to the green goal.
#
# As you move:
# - Far away -> "Cold"
# - Closer -> "Warm"
# - Very close -> "Hot"
# - Touching the goal -> "You win!"
#
# You must complete the TODO sections yourself.
#
# Read the method explanations carefully before solving each part.
#
# ============================================================

import turtle

# ============================================================
# PART 1: CREATE THE GAME WINDOW
# ============================================================

# Create the game window.
window = turtle.Screen()

# title(text)
#
# Changes the window title.
#
# Parameter:
# text
# -> The words shown at the top of the window.
window.title("Reach the Goal Exercise")

# bgcolor(color_name)
#
# Changes the background colour.
#
# Parameter:
# color_name
# -> A string such as:
#    "black"
#    "white"
#    "blue"
window.bgcolor("black")


# ============================================================
# PART 2: CREATE THE PLAYER
# ============================================================

# Create the player turtle.
player = turtle.Turtle()

# shape(shape_name)

# Changes the turtle's shape.

# Parameter:
# shape_name
# -> A string such as:
#    "arrow"
#    "circle"
#    "square"
#    "triangle"
player.shape("arrow")

# color(color_name)

# Changes the turtle's colour.

# Parameter:
# color_name
# -> A string such as:
#    "red"
#    "green"
#    "yellow"
player.color("red")

# penup()
#
# Stops the turtle from drawing lines.
#
# This method has NO parameters.
player.penup()

# speed(number)
#
# Changes animation speed.
#
# Parameter:
# number
# -> 0 is the fastest.
player.speed(0)


# ============================================================
# PART 3: CREATE THE GOAL
# ============================================================

# Create another turtle object.
goal = turtle.Turtle()

# ============================================================
# TODO:
goal.shape("circle")

# Make the goal a circle.

# Useful method:

# shape(shape_name)

# Example:
# goal.shape("square")
# ============================================================



# ============================================================
# Make the goal green.

# TODO:
goal.color("green")

# Useful method:

# color(color_name)

# Example:
# goal.color("blue")
# ============================================================



# ============================================================
# Stop the goal from drawing lines.

# TODO:
goal.penup()

# Useful method:

# penup(): prevents the Turtle object from drawing lines when
#          moving throughout the window.
# ============================================================



# ============================================================
# Move the goal to:
# x = -290
# y = 230

# TODO:
goal.goto(x=-290, y=230)

# Useful method:

# goto(x, y)

# Parameters:
# x
# -> Horizontal (Left/Right) position.

# y
# -> Vertical (Up/down) position.

# Example:
# goal.goto(100, 50)
# ============================================================




# ============================================================
# PART 4: MOVEMENT VARIABLES
# ============================================================

moving_up = False
moving_down = False
moving_left = False
moving_right = False


# ============================================================
# PART 5: MOVE THE PLAYER
# ============================================================

def move_player(dx, dy):

    # xcor()
    #
    # Gets the turtle's current x position.
    #
    # No parameters.
    current_x = player.xcor()

    # ycor()
    #
    # Gets the turtle's current y position.
    #
    # No parameters.
    current_y = player.ycor()

    # Create the new position.
    new_x = current_x + dx
    new_y = current_y + dy

    # goto(x, y)
    #
    # Moves the turtle to a position.
    player.goto(new_x, new_y)


# ============================================================
# PART 6: KEYBOARD FUNCTIONS
# ============================================================

def start_moving_up():
    global moving_up
    moving_up = True


def stop_moving_up():
    global moving_up
    moving_up = False


def start_moving_down():
    global moving_down
    moving_down = True


def stop_moving_down():
    global moving_down
    moving_down = False


def start_moving_left():
    global moving_left
    moving_left = True


def stop_moving_left():
    global moving_left
    moving_left = False


def start_moving_right():
    global moving_right
    moving_right = True


def stop_moving_right():
    global moving_right
    moving_right = False


# ============================================================
# PART 7: CHECK IF THE PLAYER WON
# ============================================================

def check_if_player_won():

    # Get player position.
    player_x = player.xcor()
    player_y = player.ycor()

    # Get goal position.
    goal_x = goal.xcor()
    goal_y = goal.ycor()

    # abs(number)
    #
    # abs means "absolute value".
    #
    # It removes negative signs.
    #
    # Examples:
    #
    # abs(-10) -> 10
    # abs(10) -> 10
    #
    # This is useful for measuring distance.

    # ========================================================
    # TODO:
    #
    # Find the x distance between the player and goal.
    #
    # Example:
    # abs(player_x - goal_x)
    # ========================================================

    # x_distance =


    # ========================================================
    # TODO:
    #
    # Find the y distance between the player and goal.
    # ========================================================

    # y_distance = 


    # ========================================================
    # TODO:
    #
    # If the player is close to the goal,
    # print "You win!"
    #
    # Useful operators:
    #
    # <
    # -> Less than.
    #
    # and
    # -> BOTH conditions must be true.
    #
    # Example:
    #
    # if x_distance < 20 and y_distance < 20:
    #     print("You win!")
    # ========================================================




# ============================================================
# PART 8: HOT AND COLD HINTS
# ============================================================

def give_hint():

    player_x = player.xcor()
    player_y = player.ycor()

    goal_x = goal.xcor()
    goal_y = goal.ycor()

    dx = abs(player_x - goal_x)
    dy = abs(player_y - goal_y)

    # ========================================================
    # COMPARISON OPERATORS
    # ========================================================
    #
    # <
    # -> Less than.
    #
    # >=
    # -> Greater than OR equal to.
    #
    # ========================================================
    # BOOLEAN WORDS
    # ========================================================
    #
    # and
    # -> BOTH conditions must be true.
    #
    # or
    # -> Only ONE condition must be true.
    #
    # ========================================================


    # ========================================================
    # TODO:
    #
    # Print "Cold" if the player is far away.
    #
    # Hint:
    # Use >= and or
    #
    # Example:
    #
    # if dx >= 100 or dy >= 100:
    #     print("Cold")
    # ========================================================




    # ========================================================
    # TODO:
    #
    # Print "Warm" if the player is getting closer.
    #
    # Hint:
    # Use < and and
    # ========================================================




    # ========================================================
    # TODO:
    #
    # Print "Hot" if the player is very close.
    # ========================================================




    # ========================================================
    # BONUS:
    #
    # Add:
    # print("VERY HOT")
    #
    # when the player is almost touching the goal.
    # ========================================================



# ============================================================
# PART 9: MAIN GAME LOOP
# ============================================================

def game_loop():

    if moving_up:
        move_player(0, 5)

    if moving_down:
        move_player(0, -5)

    if moving_right:
        move_player(5, 0)

    if moving_left:
        move_player(-5, 0)

    # ========================================================
    # TODO:
    #
    # Call the function that checks if the player won.
    #
    # Example:
    # check_if_player_won()
    # ========================================================




    # ========================================================
    # TODO:
    #
    # Call the function that gives hints.
    # ========================================================




    # ontimer(function, milliseconds)
    #
    # Runs a function again later.
    #
    # Parameters:
    #
    # function
    # -> Which function to run.
    #
    # milliseconds
    # -> How long to wait.
    #
    # Example:
    #
    # window.ontimer(game_loop, 20)

    window.ontimer(game_loop, 20)


# ============================================================
# PART 10: KEYBOARD CONTROLS
# ============================================================

# listen()
#
# Starts listening for keyboard input.
window.listen()

# onkeypress(function, key)
#
# Runs a function when a key is pressed.
#
# Parameters:
#
# function
# -> Which function to run.
#
# key
# -> Which key to listen for.
window.onkeypress(start_moving_up, "Up")
window.onkeypress(start_moving_down, "Down")
window.onkeypress(start_moving_left, "Left")
window.onkeypress(start_moving_right, "Right")

# onkeyrelease(function, key)
#
# Runs a function when a key is released.
window.onkeyrelease(stop_moving_up, "Up")
window.onkeyrelease(stop_moving_down, "Down")
window.onkeyrelease(stop_moving_left, "Left")
window.onkeyrelease(stop_moving_right, "Right")


# ============================================================
# PART 11: START THE GAME
# ============================================================

# ============================================================
# TODO:
#
# Start the game loop.
#
# Example:
# game_loop()
# ============================================================




# mainloop()
#
# Keeps the game window open.
window.mainloop()