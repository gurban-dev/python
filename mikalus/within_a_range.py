def check_range(num, lower, upper):
  # return lower <= num <= upper

  '''
  The commented out function is only applicable
  to integers because range() doesn't accept floats.

  If num is equal to "lower" or "upper", range()
  will return False.'''
  return num in range(lower, upper)

def get_valid_number(prompt_msg):
  while True:
    try:
      return float(input(prompt_msg))

      # Use the following line instead when
      # uncommenting return num in range(lower, upper).
      # return int(input(prompt_msg))
    except ValueError:
      print('Invalid input. Please enter a number.')

lower = get_valid_number('Input the lower bound for the range: ')
upper = get_valid_number('Input the upper bound for the range: ')

num = get_valid_number('Input a number: ')

print(f'check_range({num}, {lower}, {upper}): {check_range(num, lower, upper)}')