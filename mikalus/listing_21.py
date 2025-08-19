i = 1
flag = True

'''
Hypothetically, if variable "i" was equal to 51,
the program would enter both of the two if blocks
inside the while loop.'''
while flag:
  if i % 3 == 0:
    print('i:', i)
  if i % 17 == 0:
    flag = False
  i += 2