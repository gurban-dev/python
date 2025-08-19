def sum_of_squares(a, b):
  c = a**2 + b**2
  return c

def sum_of_remainder(d, e, f, g):
  h = d % e
  i = f % e
  return h + i

lst = []

def get_suffix(num):
  if num % 10 == 1 and num % 100 != 11:
    return 'st'
  elif num % 10 == 2 and num % 100 != 12:
    return 'nd'
  elif num % 10 == 3 and num % 100 != 13:
    return 'rd'
  else:
    return 'th'

for j in range(3):
  print(f'{j + 1}{get_suffix(j + 1)} iteration:')
  print('j:', j, '\n')

  k = 3

  while k > 1:
    print('k:', k)

    if j in [1, 3]:
      lst.append(sum_of_remainder(j, k, 1, 2))
    else:
      lst.append(sum_of_squares(j, k))
    k -= 1
  print('')

print('lst:', lst)