import math

def get_all_divisors(num):
  if num < 1:
    raise ValueError("Input must be a positive integer.")

  divisors = []

  for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
      divisors.append(i)

  return divisors

def calculate_sum(divisors):
  sum = 0

  for divisor in divisors:
    sum += divisor
  return sum

def isPerfectNum(num):
  divisors = get_all_divisors(num)

  sum_of_divisors = calculate_sum(divisors)

  sum_of_divisors_excluding_num = sum_of_divisors - num

  if num == sum_of_divisors_excluding_num:
    return True
  else:
    return False
  
# Use cases:
# 6 is a perfect number.

# 7 is not a perfect number.

num = 0

print(f'isPerfectNum({num}): {isPerfectNum(num)}')