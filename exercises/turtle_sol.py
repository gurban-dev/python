import turtle

# Create a goal object.
goal = turtle.Turtle()
goal.shape("circle")
goal.color("green")
goal.penup()

# Place the goal somewhere in the maze.
goal.goto(-200, -200)

# Create the player object.
player = turtle.Turtle()
player.shape("arrow")
player.color("red")

# Lift the pen so it does not draw lines when moving.
player.penup()

# Make the player a bit smaller.
player.shapesize(stretch_wid=0.75, stretch_len=0.75)

# Set starting position.
player.goto(180, 280)

# CHECK IF PLAYER WINS


def check_win():
    # Get the player's position.
    player_x = player.xcor()
    player_y = player.ycor()

    # Get the goal's position.
    goal_x = goal.xcor()
    goal_y = goal.ycor()

    # If the player is very close to the goal, they win.
    if abs(player_x - goal_x) < 20 and abs(player_y - goal_y) < 20:
        print("You win!")



# HOT AND COLD HINTS


def give_hint():
    player_x = player.xcor()
    player_y = player.ycor()

    goal_x = goal.xcor()
    goal_y = goal.ycor()

    # Distance between player and goal.
    dx = abs(player_x - goal_x)
    dy = abs(player_y - goal_y)

    # If the player is far away.
    if dx >= 100 or dy >= 100:
        print("Cold")

    # If the player is getting closer.
    elif dx < 100 and dy < 100:
        print("Warm")

    # If the player is very close.
    if dx < 50 and dy < 50:
        print("Hot")

    # Bonus: extremely close to the goal.
    if dx < 20 and dy < 20:
        print("VERY HOT")



# UPDATE GAME LOOP


def game_loop():
    if moving_up:
        move_player(0, 5)
            
    if moving_down:            
        move_player(0, -5)

    if moving_right:
        move_player(5, 0)

    if moving_left:
        move_player(-5, 0)

    # Call win check and hint system.
    check_win()
    give_hint()

    # Repeat the loop.
    window.ontimer(game_loop, 20)


# Start the updated game loop.
game_loop()