def print_maze_with_path(maze, path):
  maze_list = [list(row) for row in maze.grid]

  # Exclude the start (S) and goal (G).
  for (r, c) in path.steps[1:-1]:
    maze_list[r][c] = '*'

  print('print_maze_with_path() in\nprint_maze_path.py invoked:')
  for row in maze_list:
    print("".join(row))