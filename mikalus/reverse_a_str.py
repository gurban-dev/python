'''
The slicing operation string[::-1] in Python
reverses the order of the characters in the
string. It uses slicing syntax [start:end:step],
where:
start and end are omitted, meaning it includes the
entire string.

step is -1, which indicates traversal in reverse order,
starting from the last character to the first.
'''

def reverse_string(input_str):
  # The slicing syntax [:] outputs the entire string
  # because the start value defaults to 0 and the stop
  # value default to the length of "input_str".
  print(f'\ninput_str[:]: {input_str[:]}')

  # The following instruction is its equivalent:
  print(f'\ninput_str[:]: {input_str[0:len(input_str)]}\n')

  # [::-1] is an implicit version because the start
  # and stop values are excluded.

  # Syntax: input_str[start:stop:step]
  # return input_str[::-1]

  # Syntax: range(start, stop, step)
  for i in range(-1, -len(input_str)-1, -1):
    # Suppose input_str = 'Hello'

    # Output:
    # input_str[-1]: o
    # input_str[-2]: l
    # input_str[-3]: l
    # input_str[-4]: e
    # input_str[-5]: H
    print(f'input_str[{i}]: {input_str[i]}')

  '''
  Explicit version:
 
  Syntax: input_str[start:stop:step]
  input_str[4:-6:-1]

  Why should the start value equal 4 when 'Hello' is
  inputted?

  In order to output the string in reverse order,
  the slicing must begin from the last character
  in the string. The index that corresponds or
  pairs with that last character is 4 or
  len(input_str) - 1.

  string literal: H   e   l   l   o
  Indices:        0   1   2   3   4

  input_str = 'Hello'

  Why should the stop value be equal to -6 when 'Hello'
  is inputted?

  The stop value specifies the index where slicing
  ends (exclusive). It's exclusive because the character
  that corresponds to the index where the slicing ends,
  will not be displayed in the terminal. It is excluded.
  Negative indices count backward from the end of the
  string.

  input_str[-5] = 'H', but the stop value is exlucuded
  from the iteration, so the program must continue until
  it reaches -6.

  Why is the step value always set to -1 when reversing
  a string?
  The step value determines how slicing progresses:
  A step of -1 means moving backward through the string.

  Setting the step value to be -1 will output the
  string in reverse order (olleH instead of Hello).

  How is -len(input_str)-1 calculated for the stop
  value?
  It's the equivalent of:
  -1 * len(input_str) - 1

  -1 is mulitplied by the length of input-str, followed
  by a subtraction of 1.'''
  print(f'\n-len(input_str)-1: {-len(input_str)-1}')

  # return input_str[len(input_str)-1:-len(input_str)-1:-1]

input_str = input("Enter a string: ")

reversed_str = reverse_string(input_str)

print(f"\nOriginal String: {input_str}")

print(f"\nReversed String: {reversed_str}")