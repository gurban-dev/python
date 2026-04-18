import turtle
import tkinter as tk
import random
from collections import deque

# Configuration
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

MAZE_WIDTH = 61
MAZE_HEIGHT = 45
CELL_SIZE = 10

MOVE_SPEED = 3
COLLISION_PADDING = 7


class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [["X"] * width for _ in range(height)]

    def generate(self):
        def carve(x, y):
            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]

            if random.random() < 0.85:
                directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 < nx < self.width - 1 and 0 < ny < self.height - 1:
                    if self.grid[ny][nx] == "X":
                        self.grid[ny][nx] = " "
                        self.grid[y + dy // 2][x + dx // 2] = " "
                        carve(nx, ny)

        start_x = self.width // 2
        start_y = self.height // 2

        self.grid[start_y][start_x] = " "
        carve(start_x, start_y)

        # Extremely low loops -> harder maze
        self._add_loops(10)

        # Solid border
        for x in range(self.width):
            self.grid[0][x] = "X"
            self.grid[self.height - 1][x] = "X"

        for y in range(self.height):
            self.grid[y][0] = "X"
            self.grid[y][self.width - 1] = "X"

        # Find farthest reachable point
        exit_pos = self._farthest_cell((start_x, start_y))

        return self.grid, (start_x, start_y), exit_pos

    def _add_loops(self, attempts=10):
        for _ in range(attempts):
            x = random.randrange(1, self.width - 1)
            y = random.randrange(1, self.height - 1)

            if self.grid[y][x] == "X":
                neighbors = sum([
                    self.grid[y+1][x] == " ",
                    self.grid[y-1][x] == " ",
                    self.grid[y][x+1] == " ",
                    self.grid[y][x-1] == " "
                ])

                if neighbors >= 2:
                    self.grid[y][x] = " "

    def _farthest_cell(self, start):
        queue = deque([start])
        visited = {start}
        parent = {}

        farthest = start

        while queue:
            x, y = queue.popleft()
            farthest = (x, y)

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny][nx] == " " and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        return farthest


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