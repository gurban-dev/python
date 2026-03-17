# It is conventional to leave two empty
# lines above a class definition.
class Maze:
  '''
  An object/instance of a class contains
  attributes. In this case, the attributes
  are "rows" and "cols".

  The class constructor where the attributes
  of the class instance will be initialised
  with values.

  These values can be arguments that the class
  constructor accepts as parameters.

  In this case, the only parameter the
  constructor accepts is called "grid".  '''
  def __init__(self, grid):
    # use the parameter
    self.grid = grid

    # number of rows in grid
    self.rows = len(self.grid)

    # number of columns in grid
    self.cols = len(self.grid[0])

  def get_start_position(self):
    for row in range(self.rows):
      for col in range(self.cols):
        if self.grid[row][col] == 'S':
          return (row, col)
        
  def is_goal(self, position):
    (row, col) = position

    # Also acceptable, but not a tuple.
    # row, col = position

    if self.grid[row][col] == 'G':
      return True
    else:
      return False
    
  def is_accessible(self, position):
    (row, col) = position

    # \ is called the newline continuation character.
    if row >= 1 and col >= 1 and \
      row < self.rows and col < self.cols:
      # Returns True if self.grid[row][col]
      # is not equal to '#'.
      return self.grid[row][col] != '#'
    return False

  def get_adjacent(self, position):
    (row, col) = position

    adjacent_positions = [
      # Suppose position = (3, 4)

      # (3, 3)
      (row, col - 1),

      # (3, 5)
      (row, col + 1),

      # (4, 4)
      (row + 1, col),

      # (2, 4)
      (row - 1, col)
    ]
    return adjacent_positions

# Python list data structure.
# Python lists are declared with
# square brackets.
grid = [
  '##########',
  'S...#.##.#',
  '###.#....#',
  '#.#.#.#.##',
  '#.#...#..G',
  '#.#.####.#',
  '#.#....#.#',
  '#.#.##...#',
  '#...#..#.#',
  '##########'
]

def test():
  # Create an object of the Maze class.
  maze = Maze(grid)

  # It is important to output the value of data
  # in a program because it makes it easier to
  # debug it when a bug occurs.
  print("The maze has " + str(maze.rows) + " rows")

  print("The maze has " + str(maze.cols) + " columns")

# test()

def read_maze_from_file(filename):
  with open(filename, "r") as file:
    grid = []

    for line in file:
      # Remove the newline escape sequence.
      line = line.rstrip()

      # Append the line to grid.
      grid.append(line)
    return Maze(grid)

def test_reading_from_file():
  maze = read_maze_from_file("maze.txt")
  print("The maze has " + str(maze.rows) + " rows")
  print("The maze has " + str(maze.cols) + " columns")

# test_reading_from_file()

# path = Path([(0, 1),(0, 2)])

# path = Path()
# new_path = path + (0, 3)
# print(new_path.steps)

# path1 = Path([(1, 0), (1, 1), (1, 2), (1, 3), (2, 3)])

# path2 = Path()

# path2 += (1, 0)
# path2 += (1, 1)
# path2 += (1, 2)
# path2 += (1, 3)
# path2 += (2, 3)

# Verify that Path objects path1 and path2
# have the same steps by invoking the "steps"
# attribute.
# print(f'path1.steps: {path1.steps}\n'
#       f'path2.steps: {path2.steps}')