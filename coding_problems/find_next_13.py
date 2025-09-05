# From the datetime module, import the date and
# timedelta classes.
from datetime import date, timedelta

# Problem:
# Given a date, find the next date that is Friday the 13th.

# During coding interviews, it's important to demonstrate
# to the interviewer that you understand the problem being
# given.

# Rather than jumping straight into writing the code, we
# should ask a few questions for clarification.

# Don't assume that the input will be valid.
# Be sure to validate it.

def next_friday_13(given_date):
	# Start checking from the next day (tomorrow).

	# timedelta(days=1)
	# current = given_date + timedelta(hours=24)

	# current is a date object.

	# The subsequent link contains the documentation for date objects:
	# https://docs.python.org/3/library/datetime.html#date-objects
	current = given_date + timedelta(days=1)

	# Continue looping until the next Friday the 13th is found.
	while True:
		# Check if the following is true:
		# The day is the 13th
		# The weekday is Friday
		if current.day == 13 and current.weekday() == 4:
			return current
		current += timedelta(hours=24)

# .today() is a function, and a method.
# The .today() method is being called on date.
today = date.today()

# Example of the input:
# today: datetime.date(2025, 9, 4)
print('today:', today)

# print() is a function, but not a method.
print('next_friday_13(today):', next_friday_13(today))

'''
Why is this solution efficient?
Simply loops over the days without performing unnecesary
conversions.

Utilising the built-in datetime module rather than dependencies.
'''