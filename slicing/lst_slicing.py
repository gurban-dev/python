# A slicing expression selects a range of elements from a
# sequence.

# To obtain a slice of a list, an expression must be written
# in the following format:
# list_name[start_index:stop_index]

"""
"start_index" is the index of the first element to include in
the slice, and "stop_index" is the index marking the end of
the slice.

The expression returns a list containing a copy of the elements
from "start_index" up to (but not including) "stop_index".
"""

days_of_the_week: list[str] = [
	'Monday', 'Tuesday', 'Wednesday',
	'Thursday', 'Friday', 'Saturday',
	'Sunday'
]

"""
The below statement uses a slicing expression to get the elements
from index 2, and up to but not including, index 5.

Notice how snake case is the predominant naming convention utilised
is Python.
"""

# Slicing creates a new list (a shallow copy), not a reference.
mid_days = days_of_the_week[2:5]

# Output the slice of elements returned from the expression:
print(f'mid_days: {mid_days}')

# What if all of the days of the week must be included in the slice?

# Notice how if the start and end indexes aren't explicitly included,
# then the internally, 0 is assigned to the start_index and the length
# of the list is assigned to the stop_index.
print(f'\ndays_of_the_week[0:len(days_of_the_week)]: '
      f'{days_of_the_week[0:len(days_of_the_week)]}')

print(f'\ndays_of_the_week[:]: {days_of_the_week[:]}')

# How can everything after the first index be included in the slice?
print(f'\ndays_of_the_week[1:]: {days_of_the_week[1:]}')

# Display every second element.
print("\ndays_of_the_week[::2]:", days_of_the_week[::2])

# Reverse the list.
print("\ndays_of_the_week[::-1]:", days_of_the_week[::-1])

# How can everything before the last index be included in the slice?
print(f'\ndays_of_the_week[:len(days_of_the_week)-1]: '
      f'{days_of_the_week[:len(days_of_the_week)-1]}')

# Slicing does not raise an error if indices are out of range.
print(days_of_the_week[:100])

# Slicing works the same way for lists, strings, and other sequences.