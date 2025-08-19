from textwrap import dedent
from datetime import datetime

# Get the current date and time.
current_datetime = datetime.now()

# Extract the day of the month
day = current_datetime.day

# Determine the appropriate suffix for the day.
if 11 <= day <= 13:
    suffix = "th"
else:
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

print('day:', day, '\n')

# Format the date with the suffix
formatted_date = f"{day}{suffix} of {current_datetime.strftime('%B')}"

'''
The textwrap.dedent() method from the textwrap
module removes any common leading whitespace from
every line in the multi-line string starting from
where the line begin up until the first occurence
of actual content in the string.

Documentation:
https://docs.python.org/3/library/textwrap.html#textwrap.dedent
'''

'''
Without a multi-line string, the same f-string would need
to be written the following way which is less convenient
because a new pair of quotes are needed on each new line
as well as a newline escape sequence.'''
print(f'Hello! Today\'s date is the {formatted_date}.\n'
       'This is a multi-line statement using Python\'s f-string.\n'
       'You can embed variables like the date above seamlessly!')

'''
Notice how the leading whitespace characters
are ignored for the first eight spaces, but
are then acknowledged after that. This is
because the content is eight spaces from the
start of the line.

This is noticeable because the third line
is outputted two spaces to the right of the
first and second.'''

# Multi-line f-string with dedent().
print(dedent(
    	f'''
      	Hello! Today's date is the {formatted_date}.
       	This is a multi-line statement using Python's f-string.
        	You can embed variables like the date above seamlessly!
       '''))

'''
Without the dedent() function, the seven
whitespace characters will be included in
the terminal output because the Python
interpreter doesn't ignore them.'''
print(f'''
       Hello! Today's date is the {formatted_date}.
       This is a multi-line statement using Python f-strings.
       You can embed variables like the date above seamlessly!
       ''')