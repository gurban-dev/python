given_name = 'lovely'

# Objective:
# To understand how the characters in a string can
# be traversed.

# Iterate through the iterable "given_name".
for ch in given_name:
  # The keyword argument end='' removes the automatic
  # newline escape sequence in the output.

  # The keyword argument sep='' removes the automatic
  # whitespace character in the output.
  print(ch, '-', end='', sep='')
print('\n')