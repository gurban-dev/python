from datetime import date, timedelta

# Problem:
# Count the number of weekdays (Monday-Friday) between two dates, inclusive.

def count_weekdays(start_date, end_date):
	# Calculate the total number of days between the two dates.
	# Adding 1 ensures that both start_date and end_date are included.
	# The .days attribute converts the timedelta into an integer number
	# of days.
	days_difference = (end_date - start_date).days + 1

	# Initialize a counter for weekdays.
	count = 0

	# Loop through each day between start_date and end_date
	# range(days_difference) generates numbers from 0 up to days_difference - 1
	for i in range(days_difference):
		# Create a new date by adding i days to start_date
		current = start_date + timedelta(days=i)

		# current.weekday() returns 0 for Monday, ..., 6 for Sunday
		# If the day is Monday-Friday (0-4), count it
		if current.weekday() < 5:
			count += 1

	return count

date1 = date(2025, 9, 1)
date2 = date(2025, 9, 30)

print('count_weekdays(date1, date2):', count_weekdays(date1, date2))

'''
Why is this solution efficient?
The solution only loops once per day between the start and end dates
indicating a time complexity of O(n).

The solution doesn't create lists of dates therefore there is no
unnecessary memory usage.

It only uses a single integer counter (count) and a temporary
variable (current).
'''