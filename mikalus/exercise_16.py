def lst_of_squares(num):
  squares = list()

  for i in range(1, num):
    squares.append(i**2)
  return squares

num = int(input('Enter the number that you would like\n'
                'to see all the squares up to: '))

print(f'lst_of_squares({num}): {lst_of_squares(num)}')