# A two-dimensional list is a list that contains other lists.
# Each inner list represents one row in a grid.

# The hash symbols represent the walls of the maze.
# The whitespace characters represent the tile paths.

two_dimensional_list = [
    ['#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' '],
    ['#', '#', '#', '#', '#', '#', '#']
]

# Count the number of rows and columns in this maze.

print("two_dimensional_list:")
for row in two_dimensional_list:
    print(row)

# The two-dimensional list can also be displayed
# the folowing way, but it is less readable:
# print(two_dimensional_list)

# Indexing starts at 0 in Python.

# 'first_row' is assigned the first row.
first_row = two_dimensional_list[0]

print("\nFirst row:")
print(first_row)

# 'first_item' is assigned the first item in the first row.
first_item = two_dimensional_list[0][0]

print("\nFirst item in the first row:")
print(first_item)