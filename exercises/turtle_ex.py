# EXERCISE: REACH THE GOAL

# Goal:
# Move the player to the green circle to win the game.

# You will complete a few small pieces of code.
# Read the comments carefully and fill in the TODO parts.



# PART 1: CREATE THE GOAL


# Create a goal object.
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()

# Place the goal somewhere in the maze.
goal.goto(x=-200, y=-200)



# PART 2: CHECK IF PLAYER WINS

def check_if_player_won():
    # Get the player's position.
    player_x = player.xcor()
    player_y = player.ycor()

    # Get the goal's position.
    goal_x = goal.xcor()
    goal_y = goal.ycor()

    # TODO:
    # Complete the condition below so that:
    # If the player is VERY CLOSE to the goal,
    # the program prints "You win!"

    # Replace ? with a number like 20.

    # player_x = 10
    # goal_x = 0

    # 10 - 0 -> 10 -> abs(10) -> 10

    # 0 - 10 -> -10 -> abs(-10) -> 10

    # How can I find the difference between player_x and goal_x?

    if abs(player_x - goal_x) < 20 and abs(player_y - goal_y) < 20:
        print("You win!")



# PART 3: HOT AND COLD HINTS


def give_hint():
    player_x = player.xcor()
    player_y = player.ycor()

    goal_x = goal.xcor()
    goal_y = goal.ycor()

    # Distance between player and goal.
    dx = abs(player_x - goal_x)
    dy = abs(player_y - goal_y)

    # TODO:
    # Add a "Cold" message when the player is far away.
    # Hint: use >= and the word "or"

    if dx >= 100 or dy >= 100:
        print("Cold")

    # If the player is getting closer.
    if dx < 100 and dy < 100:
        print("Warm")

    # If the player is very close.
    if dx < 50 and dy < 50:
        print("Hot")

    # BONUS:
    # Can you add "VERY HOT" when the player is almost touching?
    # Try using a smaller number like 20.



# PART 4: CONNECT EVERYTHING


# Find your existing game_loop() function in the file.
# Inside it, add these two lines at the END of the function:

# check_win()
# give_hint()

# Your final game_loop should look something like this:

"""
def game_loop():
    if moving_up:
        move_player(0, 5)
            
    if moving_down:            
        move_player(0, -5)

    if moving_right:
        move_player(5, 0)

    if moving_left:
        move_player(-5, 0)

    # Call your new functions here.
    check_win()
    give_hint()

    window.ontimer(game_loop, 20)
"""


# WHAT YOU SHOULD SEE

# As you move:
# - Far away -> "Cold"
# - Closer -> "Warm"
# - Very close -> "Hot"
# - On the goal -> "You win!"

# Try moving the goal to a new position to test again!