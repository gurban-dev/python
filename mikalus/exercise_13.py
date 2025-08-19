# Define a function named 'pascal_triangle' that generates Pascal's Triangle up to row 'n'
from textwrap import dedent


def pascal_triangle(no_of_rows):
  # Initialize the first row of Pascal's Triangle
  # with value 1 as a starting point.
  trow = [1]
  
  # Create a list 'y' filled with zeros to
  # be used for calculations.
  y = [0]

  # Iterate through a range starting from 0 up to
  # the maximum of 'n' or 0 (taking the maximum
  # to handle negative 'n').
  for i in range(max(no_of_rows, 0)):
    print(trow)

    '''
    Update the current row based on the previous
    row by calculating the next row using list
    comprehension.
    
    [l + r for l, r in zip(trow + y, y + trow)]
    iterates over each pair (l, r) produced by
    zip() and calculates their sum (l + r).

    The result is a new list where each element is
    the sum of paired elements from the input lists.
    
    See python/list_comprehension.py for greater detail.

    1st iteration:
    trow + y:
    [1] + [0] -> [1, 0]

    y + trow:
    [0] + [1] -> [0, 1]

    list(zip([1, 0], [0, 1])) ->
    an iterator of tuples (1, 0) and (0, 1)

    l references the first element of each
    pair returned by zip.

    r references the second element of each
    pair returned by zip.

    l = 1 r = 0
    l + r -> 1 + 0 -> 1
    1 is then added to the new list that'll be
    returned.'''
    trow = [l + r for l, r in zip(trow + y, y + trow)]

    # Print the current row of Pascal's Triangle.
    # print(dedent(
    #   f'''\n\
    #     y: {y}
    #     zip({trow} + {y}, {y} + {trow}):
    #     {list(zip(trow + y, y + trow))}
    #   ''')
    # )

    # Image of Pascal's triangle:
    # https://www.mathsisfun.com/numbers/images/pascals-triangle-doubles.svg

  # Return True if 'no_of_rows' is greater
  # than or equal to 1, else return False.
  return no_of_rows >= 1

# Generate Pascal's Triangle up to row 6
# by calling the 'pascal_triangle' function.

no_of_rows = 5

pascal_triangle(no_of_rows)

# List concatenation

# Output:
# [1] + [0]: [1, 0]
# print('[1] + [0]:', [1] + [0])

# Output:
# [('a', 'b'), ('c', 'd')]
# print('list(zip([\'a\', \'b\'], [\'c\', \'d\']):',
#       list(zip([('a', 'c'), ('b', 'd')])))

# Output:
# list(zip([1, 0], [0, 1])): [(1, 0), (0, 1)]
# print('list(zip([1, 0], [0, 1])):', list(zip([1, 0], [0, 1])))

# Tuple concatenation

# Output:
# (1, 0) + (0, 1): (1, 0, 0, 1)
# print('(1, 0) + (0, 1):', (1, 0) + (0, 1))