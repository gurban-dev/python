# A two-dimensional list is a list that contains other lists.
# Each inner list represents one row in a grid.

two_dimensional_list = [
    ['#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' '],
    ['#', '#', '#', '#', '#', '#', '#']
]

print("two_dimensional_list:")
for row in two_dimensional_list:
    print(row)

# Indexing starts at 0 in Python.

# 'first_row' is assigned the first row.
first_row = two_dimensional_list[0]

print("\nFirst row:")
print(first_row)

# 'first_item' is assigned the first item in the first row.
first_item = two_dimensional_list[0][0]

print("\nFirst item in the first row:")
print(first_item)