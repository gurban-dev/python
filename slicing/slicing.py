# A slicing expression selects a range
# of elements from a sequence.

# To obtain a slice of a list, an expression
# must be written in the following format:
# list_name[start : end]

"""
"start" is the index of the first element in
the slice, and "end" is the index marking the
end of the slice.

The expression returns a list containing a copy of the
elements from "start" up to (but not including) "end".
"""

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday']

"""
The below statement uses a slicing expression to
get the elements from indexes 2 up to, but not
including, 5.
Notice how snake case is the predominant naming
convention utilized is Python.
"""
mid_days = days[2:5]

# Output the slice of elements returned from the
# expression:
print(f'mid_days: {mid_days}')