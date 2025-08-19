def exponentiation(lst , mode):
  if mode == "forward":
    value = lst.pop(0)
  
    while lst:
      # 1st iteration:
      # value = 1 ** 2 (1 ^ 2) -> 1

      # 2nd iteration:
      # value = 1 ** 3 (1 ^ 3) -> 1
      value **= lst.pop(0)
    return value
  elif mode == "backward":
    # Removes the last element/item from "lst"
    # because pop() is not passed any argument.

    # pop() and pop(0) will both return the
    # element/item they remove.
    value = lst.pop()

    while lst:
      # 1st iteration:
      # value = 3 ** 2 (3 ^ 2) -> 9

      # 2nd iteration:
      # value = 9 ** 1 (9 ^ 1) -> 9
      value **= lst.pop()

    # Returns the most recent value
    # of the variable "value".
    return value
  else:
    return "Error"

print(exponentiation([1 , 2 , 3], "forward"))
print(exponentiation([1 , 2 , 3], "backward"))