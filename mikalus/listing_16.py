# pop() without a specified position
# simply removes the last element
# inside the container.

# pop() returns the element that it has
# removed.
lst = [1, 5, 3]

i = 1
result = 0

# lst = []

# lst evaluates to False
# print('bool(lst):', bool(lst))

while lst:
  current = lst.pop()

  result += current * i
  i += 1

print('result:', result)