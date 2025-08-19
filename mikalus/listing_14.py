def f(x, y):
  '''
  First iteration:
  i is equal to 2.

  x = i
  y = i * 2

  return 2 * (4 + 1)

  Second iteration:
  i is equal to 3.

  x = i
  y = i * 2

  return 3 * (6 + 1)
  '''
  return x * (y + 1)

'''
Assigns 2 and 3 to variable "i" because the
iterable is a list rather than a sequence of
integers returned by range(2, 3).

range(2, 3) returns only 2 and excludes 3, so
"i" would only be assigned 2:
for i in range(2, 3):

Iterating over the tuple (2, 3) would assign 2
and 3 to variable "i".
for i in (2, 3):
'''
for i in [2, 3]:
  print('\ni:', i)

  print('f(i, i*2):', f(i, i*2))