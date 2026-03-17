# Syntax:
# string[start_index:stop_index:step_value]

# For slicing with a negative step:
# start_index: the index where slicing starts (inclusive).
#              If omitted, it defaults to the end of the string (len(string) - 1).

# stop_index:  the index where slicing stops (exclusive).
#              If omitted, it defaults to one before the beginning of the string (-1).

# step_value:  the increment between elements. Negative means move backwards.

# If step_value is positive, it includes characters while current_index < stop.

# If step_value is negative, it includes characters while current_index > stop.

# The stop_index is interpreted as 4, so current_index is not less than the
# stop. None of the characters in "Hello" will be outputted.
print("\"Hello\"[4:-1:-1]", "Hello"[4:-1:-1])

# Reversing "Hello" by explicitly specifying the start and stop indexes:
print("\"Hello\"[4:-6:-1]:", "Hello"[4:-6:-1])

# Start index 4 corresponds to the last character 'o'.
# Stop index -6 is one before the first character (essentially stops before 'H').
# The indices of "Hello" are:
# -5  -4  -3  -2  -1
#  H   e   l   l   o
# The slice [4:-6:-1] goes from index 4 down to index -5 (exclusive) in reverse.

# Example:
s = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

# Slice the string backwards taking every 2nd character.
print('Sliced string [::-2]:\n', s[::-2], sep='')