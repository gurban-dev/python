'''
Suppose you had to calculate the total number
of ways a mini-deck of 4 cards could be arranged.

Since there are 4 cards in the mini-deck, there
are 4 factorial or 4! number of ways it can be
arranged, which equals 24.'''

def get_factorial(num):
  product = num

  # range(start, stop, step)
  for i in range(num - 1, 1, -1):
    product *= i

  return product

def get_valid_number():
  while True:
    try:
      return int(input('Input a number: '))
    except ValueError:
      print('Invalid input. Please enter a number.')

num = get_valid_number()

print(f'get_factorial({num}): {get_factorial(num)}')