from collections import deque
from path import Path
from get_suffix import get_suffix

def output_queue(queue):
  for path_object in queue:
    print(path_object.steps)
  print('')

def get_shortest_path(maze):
  start = maze.get_start_position()

  # Output for maze_1.py:
  # start: (1, 0)
  print('start:', start, '\n')

  # Create a Path object containing
  # the start position:
  # path = Path([(1, 0)])
  path = Path([start])

  '''
  deque() is a function from the collections
  module in Python. It creates a double-ended
  queue, which is a data structure that allows
  you to efficiently add or remove elements
  from both ends (the beginning and the end).'''
  queue = deque()

  # Append the Path object called "path" to
  # the queue. Keep in mind that the name
  # didn't necessarily need to be "path".
  queue.append(path)

  '''
  Declare a list data structure to keep
  track of all the positions within the
  maze that have been previously visited.
  The square brackets indicates that this
  is a list data structure.'''
  visited = [start]

  iterNum = 1

  # The while loop will continue iterating
  # so long as the queue is not empty.
  while queue:
    '''
    On each iteration:
    1. Dequeue the first path from the queue.

    2. Check if the last position in the path
       is the goal. If so, return the path.

    3. Otherwise, explore all accessible adjacent
       positions that have not been visited yet.'''

    '''
    Remove and return the first path pair
    from the queue. Elements in a queue
    are enqueued to the back of the queue,
    and dequeued from the front to honour
    first in first out.''' 
    path = queue.popleft()

    iteration_str = f'{iterNum}{get_suffix(iterNum)} while loop iteration'
    print(f'\033[1m{iteration_str}\033[0m')

    iterNum += 1

    '''
    "path" is an object of the Path class
    declared in the path.py module.

    "steps" is an instance variable declared
    in the Path class.'''
    print('path.steps:', path.steps, '\n')

    print('path.steps[-1]:', path.steps[-1], '\n')

    # path.steps[-1] obtains the last tuple
    # in the list.
    position = path.steps[-1]

    print('position:', position, '\n')

    # Remember that the last element in the queue,
    # is the most recent/latest one that was
    # enqueued/added.
    if maze.is_goal(position):
      return path

    print('maze.get_adjacent(position):',
          maze.get_adjacent(position), '\n')

    '''
    Consider the tiles to the top, bottom, left, and right.
    Notice that with example maze_1.py, tiles (4, 4) and
    (5, 3) were the adjacent files during the 7th iteration.

    During this iteration, only (5, 3) does not become part
    of path.steps because popleft() removes and returns the
    item at the beginning of the queue.''' 
    for adjacent in maze.get_adjacent(position):
      if maze.is_accessible(adjacent) and adjacent not in visited:
        '''
        Breadth first search is designed to explore nodes
        level by level, ensuring that each node is processed
        only once. Without marking nodes as visited, the
        algorithm might revisit the same node multiple times.'''
        visited.append(adjacent)

        print('adjacent:', adjacent)

        '''
        Forming a new path by adding the current one
        and the adjacent position is necessary because
        it makes it possible to maintain a sequence of
        positions taken to reach the goal node in the
        maze.'''

        # path + invokes the __add__() method
        # in the Path class.

        # new_path = <path.Path object at memory_address> + (1, 1)
        new_path = path + adjacent

        print('new_path.steps:', new_path.steps)

        # Append the new Path object to the end
        # of the queue.
        queue.append(new_path)

        print('\noutput_queue(queue):')
        output_queue(queue)

  # If the flow of the program reaches this point,
  # it can be affirmed that there isn't a solution.
  raise Exception("This maze has no solution")