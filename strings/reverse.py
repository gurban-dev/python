string = input('Enter any string: ')

print('\nstring:', string)

# Syntax:
# range(start, stop (exclusive), step)
for i in range(len(string)-1, -1, -1):
  print('\ni:', i)

  print(f'{string}[{i}]: {string[i]}')