# User-defined function

# The "total_days" parameter will be assigned
# the value of the argument that was passed.
def readable_timedelta(total_days):
  # // (two-forward slashes indicates) that
  # integer/floor division is being performed.
  no_of_weeks = total_days // 7

  no_of_days = total_days % 7

  # Returning an f-string to the point in the
  # program where this function was invoked or
  # called.
  return (f'{no_of_weeks} week(s) and {no_of_days} day(s)')

# 11 is being passed as an argument.
print('readable_timedelta(11):', readable_timedelta(11), '\n')

print('readable_timedelta(22):', readable_timedelta(22), '\n')