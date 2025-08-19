import math

def get_all_divisors(num):
  divisors = []

  for i in range(1, int(math.sqrt(num)) + 1):
    if num % i == 0:
      divisors.append(i)

  return divisors

def is_prime(num):
  if num < 1:
    return False
  
  if len(get_all_divisors(num)) != 2:
    return False
  return True

num = 43

print(f'is_prime({num}): {is_prime(num)}')