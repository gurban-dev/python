'''
If a number is divisible by 9, then the
sum of its digits is also divisible by 9.

Cannot utilise:
modulo, floor/integer division, or float division

def divisible_by_nine(whole_num):
  # Returns True if the number is divisible by 9.
  return whole_num % 9 == 0

def sum_is_divisible_by_nine(whole_num):
  sum_of_digits = sum(int(digit) for digit in str(whole_num))

  # Returns True if the sum of the number's
  # digits can be evenly divided by 9.
  return sum_of_digits % 9 == 0

print(f'divisible_by_nine(900): '
      f'{divisible_by_nine(900)}')

print(f'sum_is_divisible_by_nine(900): '
      f'{sum_is_divisible_by_nine(900)}')
'''

def divisible_by_9(number):
  # Suppose number is equal to 18.
  # while 18 >= 10:

  # or use len(str(number))
  while number >= 10:
    sum_digits = 0

    # The sum of the number's digits
    # is computed in the for loop.

    # for digit in str(18):
    for digit in str(number):
      # 1st iteration:
      # sum_digits = 0 + int('1') -> 1

      # 2nd iteration:
      # sum_digits = 1 + int('8') -> 9
      sum_digits += int(digit)

    # 'Sum of the digits of 18: 9'
    print('Sum of the digits of {}: {}'.format(number, sum_digits))

    # number = 9
    number = sum_digits

    print('number:', number)

  # Returns True if the "number" variable is
  # equal to 9. Otherwise, it returns False.
  return number == 9

print(f'divisible_by_9(18): {divisible_by_9(18)}')