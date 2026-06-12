

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