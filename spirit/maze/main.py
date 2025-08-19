from maze import Maze
from get_shortest_path import get_shortest_path
from print_maze_path import print_maze_with_path

def main():
  with open("maze_1.txt", "r") as file:
    '''
    Iterate through the lines in the specified
    file. The lines are read as strings.

    On each iteration, a copy of the string
    without trailing whitespace characters will
    be returned.
    
    E.g.
    0123456789
       ####   

    rstrip() will only remove the whitespace
    characters in indices 7, 8, and 9.'''
    grid = [line.rstrip() for line in file]

    maze = Maze(grid)

  path = get_shortest_path(maze)

  '''
  The instance variable "steps" stores a list
  data structure consisting of tuples where
  each tuple is made up of a row and column
  number.

  The row and column number represents the tile
  position that is part of the path from S to G.'''
  print(f'main.py path.steps:\n{path.steps}\n')

  print_maze_with_path(maze, path)

if __name__ == '__main__':
  main()