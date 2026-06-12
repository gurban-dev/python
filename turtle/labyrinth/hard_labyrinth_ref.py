import turtle
import tkinter as tk
import random
from collections import deque

from config import CELL_SIZE


class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.walls = []

        self.drawer = turtle.Turtle()
        self.drawer.shape("square")
        self.drawer.color("black")
        self.drawer.penup()
        self.drawer.speed(0)

        self._draw()

    def _draw(self):
        start_x = - (MAZE_WIDTH * CELL_SIZE) // 2
        start_y = (MAZE_HEIGHT * CELL_SIZE) // 2

        for row in range(MAZE_HEIGHT):
            for col in range(MAZE_WIDTH):
                if self.grid[row][col] == "X":
                    x = start_x + col * CELL_SIZE
                    y = start_y - row * CELL_SIZE

                    self.drawer.goto(x, y)
                    self.drawer.shapesize(0.35, 0.35)
                    self.drawer.stamp()
                    self.walls.append((x, y))

    def is_collision(self, x, y):
        for wx, wy in self.walls:
            if abs(x - wx) < COLLISION_PADDING and abs(y - wy) < COLLISION_PADDING:
                return True
        return False


class MazeRenderer:
    def draw(self, maze):
        pass


class Player:
    def __init__(self, start_pos):
        self.turtle = turtle.Turtle()
        self.turtle.shape("circle")
        self.turtle.color("red")
        self.turtle.penup()
        self.turtle.shapesize(0.45, 0.45)
        self.turtle.goto(start_pos)

    def move(self, dx, dy, maze):
        new_x = self.turtle.xcor() + dx
        new_y = self.turtle.ycor() + dy

        if not maze.is_collision(new_x, new_y):
            self.turtle.goto(new_x, new_y)

    def distance_to(self, pos):
        return self.turtle.distance(pos)


class Game:
    def __init__(self):
        self.window = turtle.Screen()
        self.window.title("Impossible Labyrinth")
        self.window.bgcolor("white")
        self.window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

        generator = MazeGenerator(MAZE_WIDTH, MAZE_HEIGHT)
        grid, start_cell, exit_cell = generator.generate()

        self.maze = Maze(grid)

        self.player = Player(self._cell_to_screen(start_cell))
        self.goal_pos = self._cell_to_screen(exit_cell)

        self.goal = turtle.Turtle()
        self.goal.shape("square")
        self.goal.color("green")
        self.goal.penup()
        self.goal.shapesize(0.5, 0.5)
        self.goal.goto(self.goal_pos)

        self.running = True
        self.movement = {"up": False, "down": False, "left": False, "right": False}

        self._bind_keys()
        self._loop()

    def _cell_to_screen(self, cell):
        start_x = - (MAZE_WIDTH * CELL_SIZE) // 2
        start_y = (MAZE_HEIGHT * CELL_SIZE) // 2

        col, row = cell
        x = start_x + col * CELL_SIZE
        y = start_y - row * CELL_SIZE
        return (x, y)

    def _bind_keys(self):
        self.window.listen()

        self.window.onkeypress(lambda: self._set("up", True), "Up")
        self.window.onkeyrelease(lambda: self._set("up", False), "Up")

        self.window.onkeypress(lambda: self._set("down", True), "Down")
        self.window.onkeyrelease(lambda: self._set("down", False), "Down")

        self.window.onkeypress(lambda: self._set("left", True), "Left")
        self.window.onkeyrelease(lambda: self._set("left", False), "Left")

        self.window.onkeypress(lambda: self._set("right", True), "Right")
        self.window.onkeyrelease(lambda: self._set("right", False), "Right")

    def _set(self, key, val):
        self.movement[key] = val

    def _loop(self):
        if not self.running:
            return

        dx, dy = 0, 0

        if self.movement["up"]:
            dy += MOVE_SPEED
        if self.movement["down"]:
            dy -= MOVE_SPEED
        if self.movement["left"]:
            dx -= MOVE_SPEED
        if self.movement["right"]:
            dx += MOVE_SPEED

        self.player.move(dx, dy, self.maze)

        if self.player.distance_to(self.goal_pos) < 8:
            self.running = False
            self._popup()
            return

        self.window.ontimer(self._loop, 20)

    def _popup(self):
        root = self.window._root
        popup = tk.Toplevel(root)
        popup.title("Victory")
        popup.geometry("350x180")

        tk.Label(
            popup,
            text="You escaped the impossible labyrinth!",
            font=("Arial", 12),
            wraplength=300
        ).pack(pady=20)

        tk.Button(popup, text="Restart", command=lambda: self._restart(popup)).pack(pady=5)
        tk.Button(popup, text="Quit", command=root.destroy).pack(pady=5)

    def _restart(self, popup):
        popup.destroy()
        turtle.clearscreen()
        Game()


if __name__ == "__main__":
    Game()
    turtle.done()

# 1. Separate Game Logic from Rendering
#    The Maze class handles two responsibilties:
#    a. Stores maze data.
#    b. Draws the maze with Turtle.

# The problem is that game logic is tightly coupled with Turtle
# graphics.

# The maze should only know about walls and paths.
# This follows the Single Responsibility Principle (SRP).

# 2. All constants should be put inside a file named config.py
#    because configuration should be centralised instead of
#    having to search through multiple files.

# 3. Create a maze_generator.py file and move the MazeGenerator
#    class into there because Maze generation is a completely
#    separate concern from rendering.

#    Separating the maze algorithm from the tool used to implement
#    it (Turtle, Pygame, etc.) makes it reusable.