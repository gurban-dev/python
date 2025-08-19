i = 0
lst = []

while i < 3:
  lst.append([])

  j = 0

  # Exited when "j" is no longer
  # less than "i".
  while j < i:
    # "j" cannot be greater than or equal to "i"
    # when the flow of the program is in this
    # while loop.

    print('Inner while loop\n\
lst before:', lst, '\ni:', i)

    lst[i].append(j)

    print('lst after:', lst, '\n')

    j += 1

  i += 1

print('lst:', lst)