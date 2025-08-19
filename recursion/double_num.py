'''
The double() function accepts three parameters:
value
recursion_count
no_of_recursions
'''
def double(value, recursion_count, no_of_recursions):
  print('Current value:', value)

  if recursion_count == no_of_recursions:
    return value
  else:
    # value = value * 2
    value *= 2

    recursion_count += 1

    return double(value, recursion_count, no_of_recursions)

initial_value = 1
no_of_recursions = 12

double(initial_value, 0, no_of_recursions)  