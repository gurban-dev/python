a = 50
b = '10'

# Integer/floor division
c = 50 // len(b)

print('Before for loop.')
print(f'c: {c}')

print('\nIn for loop.')
for i in range(2):
  # c = 25 % 9 -> 7
  # c = 7

  # c = 7 % 9 -> -2

  '''
  7 is congruent to 7 mod 9 because
  7 - (7) = 0 which is divisble by 9.

  7 is congruent to -2 mod 9 because
  7 - (-2) = 9 which is divisble by 9.
  '''

  # c = 7 % 9

  # c = c % 9
  c %= 9
  print(f'c: {c}')

print('\nAfter for loop.')
print(f'c: {c}')