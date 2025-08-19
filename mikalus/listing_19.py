lst1 = [1, 2, 3]
lst2 = [1, 1, 1, 2]

result = lst1.pop(0)

for i in range(len(lst1)):
  print('i:', i)

  result += lst2[i]

  # Iterates four times because "lst2"
  # contains four elements/items.
  for i in lst2:
    result += i

print('result:', result)