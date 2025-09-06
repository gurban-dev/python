import pdb

'''
Commands in pdb:
n -> next line
s -> steps into a function
c -> continue until the next breakpoint
p <variable_name> -> prints the variable value
q -> quit the debugger
'''

def divide(num1, num2):
  # The subsequent line acts as a breakpoint.
  pdb.set_trace()

  result = num1 // num2

  # Command to output the value of "result".
  # p result
  pdb.set_trace()

  return result

result = divide(10, 2)

print('result:', result)