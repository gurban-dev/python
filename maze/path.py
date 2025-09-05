# Represents a sequence of steps or a
# path that must be taken to reach the
# goal position, denoted G in the maze.
class Path:
  def __init__(self, steps=[]):
    # Instance variable.
    self.steps = steps

  # The "+" operator invokes this method.
  def __add__(self, position):
    print('path.py position:', position, '\n')

    # 1st while loop iteration:
    # Path([(1, 0)] + [(1, 1)])
    return Path(self.steps + [position])