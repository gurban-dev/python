def a(x):
  return 2*x

def b(x):
  return x+1

lst = ['a', 'b', 'a']
value = 3

while lst:
  action = lst.pop()

  if action == "a":
    value = a(value)
  elif action == "b":
    value = b(value)

print ('value:', value)